from flask import Flask, request, render_template, redirect, url_for, session
import numpy as np
import joblib
from feature import FeatureExtraction
import warnings
import os
from flask_sqlalchemy import SQLAlchemy
warnings.filterwarnings('ignore')

app = Flask(__name__)
# Use explicit SQLite database for Render deployment (file-based DB in app root)
# If DATABASE_URL env var is provided, it will override this value.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///phishnet.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key_here')

# Initialize SQLAlchemy (keeps DB models & functionality unchanged)
db = SQLAlchemy(app)

# Load ML model
BASE_DIR   = os.path.dirname(__file__)            # …/backend
# For Render deployment the model is placed at the repository root. Use the
# absolute path Render uses for the project. This ensures the app loads the
# model saved at /opt/render/project/src/model.pkl (repo root), not under
# backend/../ml_model.
def find_model_path():
    """Return the first existing model path.

    Order of preference:
      1. ./model.pkl (when running from repo root)
      2. ../model.pkl  (when running from backend/)
      3. /opt/render/project/src/model.pkl (Render)
    """
    # Try a few likely locations. Order matters: try relative paths first, then Render path.
    candidates = [
        os.path.abspath(os.path.join(BASE_DIR, '..', 'model.pkl')),         # ../model.pkl (up one level to project root)
        os.path.abspath(os.path.join(BASE_DIR, 'model.pkl')),               # backend/model.pkl (current directory)
        os.path.abspath(os.path.join(BASE_DIR, '.', 'model.pkl')),          # backend/./model.pkl (explicit current)
        '/opt/render/project/src/model.pkl',                                 # Render absolute path
    ]
    for p in candidates:
        try:
            if os.path.exists(p):
                return p
        except Exception:
            continue
    return None


# Determine model path and load if available. App will continue to run even if
# the model is missing; the prediction endpoint should handle that case.
MODEL_PATH = find_model_path()

# Make model loading safe - allow app to start even if model isn't available
gbc = None
if MODEL_PATH is None:
    print("ERROR: No model file found. Tried locations:")
    for p in [
        os.path.abspath(os.path.join(BASE_DIR, '..', 'model.pkl')),         # project root
        os.path.abspath(os.path.join(BASE_DIR, 'model.pkl')),               # backend folder
        os.path.abspath(os.path.join(BASE_DIR, '.', 'model.pkl')),          # explicit ./
        '/opt/render/project/src/model.pkl',                                 # Render path
    ]:
        print("  - ", p)
    print("Please place model.pkl at the project root or the Render path.")
else:
    print(f"Loading model from: {MODEL_PATH}")
    try:
        gbc = joblib.load(MODEL_PATH)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"ERROR: Model failed to load from {MODEL_PATH} - {e}")
        print("App will start but prediction endpoint will return an error until model is fixed.")

# Ensure database tables are created at startup. If you have models defined
# in other modules, import them before calling create_all so SQLAlchemy knows
# about them. Example: from .models import *
with app.app_context():
    try:
        # create_all will create any missing tables for declared models
        db.create_all()
    except Exception:
        # If DB initialization fails, continue but log the error in real usage
        pass

# Utility to ensure URL has a scheme
def validate_url(input_url):
    if not input_url.startswith("http://") and not input_url.startswith("https://"):
        return "http://" + input_url
    return input_url

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        raw_url = request.form.get("url")
        url = validate_url(raw_url)

        # If model isn't loaded, return a friendly error instead of crashing
        if gbc is None:
            error_msg = "Model is not available. Please try again later."
            return render_template("index.html", xx=None, url=url, error=error_msg), 503

        # Extract features and predict
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1, 30)

        y_pro_phishing = gbc.predict_proba(x)[0, 0]
        y_pro_non_phishing = gbc.predict_proba(x)[0, 1]

        # Store results in session
        session["xx"] = round(y_pro_non_phishing, 2)
        session["url"] = url

        return redirect(url_for("index"))

    # Read from session and clear after showing
    xx = session.pop("xx", None)
    url = session.pop("url", None)
    return render_template("index.html", xx=xx, url=url)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/awareness")
def awareness():
    return render_template("awareness.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
