from flask import Flask, request, render_template, redirect, url_for, session
import numpy as np
import pickle
from feature import FeatureExtraction
import warnings
import os
warnings.filterwarnings('ignore')

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key in production

# Load ML model
BASE_DIR   = os.path.dirname(__file__)            # …/backend
MODEL_PATH = os.path.join(BASE_DIR, '..', 'ml_model', 'model.pkl')

with open(MODEL_PATH, "rb") as file:
    gbc = pickle.load(file)

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
