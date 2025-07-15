# 🐟 PhishNet – AI‑powered Phishing‑Detection Service

[![Build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)](#)
[![Python](https://img.shields.io/badge/python-3.10-blue?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-purple?style=flat-square)](#)

An end‑to‑end phishing‑detection platform that uses classical ML to identify malicious URLs.  
Comes with a clean multi-page UI and can be deployed with ease using Flask and Render.

---

## 📁 Folder Structure

PhishNet/
├── backend/
│ ├── static/
│ │ └── styles.css # Custom CSS styles
│ ├── templates/
│ │ ├── index.html # Home page with URL form
│ │ ├── about.html # About project
│ │ ├── contact.html # Contact info
│ │ └── awareness.html # Awareness page on phishing
│ ├── init.py # Flask app init (optional)
│ ├── app.py # Main Flask application
│ ├── feature.py # URL feature extraction logic
│ └── Phishing URL Detection.ipynb # Analysis & experiments
│├── ml_model/
│ ├── model.pkl # Trained ML model (scikit-learn)
│ ├── phishing.csv # Dataset used for training
│ └── Phishing URL Detection.ipynb # Training notebook
│
├── requirements.txt # Python dependencies
├── runtime.txt # Python version for Render
├── Procfile # Deployment config for Render
├── venv/ # (optional) Virtual environment
├── venv_phishnet/ # (optional) Another venv (avoid pushing to Git)
---

## 🚀 Features

| Feature            | Description |
|--------------------|-------------|
| 🔗 URL Detection    | Lexical feature extraction using handcrafted rules |
| 🧠 ML Model         | Trained with RandomForestClassifier or Logistic Regression |
| 🌐 Web UI           | Multi-page Bootstrap-based HTML interface |
| 📬 Flask API        | JSON prediction endpoint at `/predict` |
| 🛠 Model Persistence | Model stored as `.pkl`, loaded on server start |
| 🧪 Notebooks        | Jupyter notebooks for training and testing |
| 🧾 Awareness        | Additional phishing info via `awareness.html` |

---

## 🛠 Tech Stack

- Python 3.10.0
- Flask + Jinja2
- scikit-learn
- Pandas, NumPy
- Bootstrap 5 (via CDN)
- Gunicorn (for production server)
- Render (for cloud deployment)

---

## 🧪 Local Setup

1. 🔧 Create and activate a virtual environment:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate📦

1. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
▶️ Start the Flask server:

bash
Copy
Edit
cd backend
python app.py
Open your browser at http://localhost:5000

🌐 Pages
Route	Description
/	Home page – URL form
/about	About the project
/contact	Contact details
/awareness	Phishing awareness tips

📡 API Endpoint
POST /predict

Headers:

json
Copy
Edit
Content-Type: application/json
Body:

json
Copy
Edit
{ "url": "http://suspicious.com" }
Response:

json
Copy
Edit
{
  "prediction": "phishing",
  "features": {
    "url_length": 54,
    "num_dots": 3,
    ...
  }
}
🧠 Model Info
Model Type: scikit-learn (RandomForestClassifier or LogisticRegression)

Training Data: phishing.csv

Pickled Model: ml_model/model.pkl

You can retrain the model using the notebook in ml_model/Phishing URL Detection.ipynb.
