from flask import Flask, request, render_template, redirect, url_for, session
import numpy as np
import pickle
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
MODEL_PATH = '/opt/render/project/src/model.pkl'

# Make model loading safe - allow app to start even if model isn't available
gbc = None
try:
    with open(MODEL_PATH, "rb") as file:
        gbc = pickle.load(file)
except Exception as e:
    print(f"Warning: Model failed to load from {MODEL_PATH} - {e}")
    print("App will start but prediction endpoint will return error 503 until model is fixed")

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
