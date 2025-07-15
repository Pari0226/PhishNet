# 🐟 PhishNet – AI‑Powered Phishing Detection Service

[![Build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)](#)
[![Python](https://img.shields.io/badge/python-3.10-blue?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-purple?style=flat-square)](#)

PhishNet is an AI-powered phishing detection web app that identifies malicious URLs using a trained machine learning model. It features a clean Flask-based interface, awareness content, and API endpoints for integration. Designed to be fast, educational, and deployment-ready.

---

## 🌐 Live Demo

> Deployed via Render (free tier)  
> 🔗 https://phishnet.onrender.com *(link coming soon)*

---

## ✨ Features

| Category        | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| 🔗 URL Detection | 30+ lexical & host-based features extracted from URLs                      |
| 🧠 ML Model      | Gradient Boosting Classifier trained on phishing.csv dataset               |
| ⚙️ Feature Logic | `feature.py` handles all feature extraction logic cleanly                  |
| ⚡ API Endpoints | `/predict-url` for real-time predictions (returns JSON result)             |
| 🖥️ Web Interface | Flask + **Tailwind CSS** UI with responsive layout                         |
| 📚 Awareness      | Static pages on phishing awareness & online safety                        |
| 🛡️ Stateless     | No database – real-time in-memory prediction                              |
| 🚀 Render Ready  | Docker-free, 1-click deployment on Render with minimal config              |


## 📁 Project Structure
PhishNet/
├── backend/
│ ├── static/
│ │ └── styles.css # Custom CSS styles
│ ├── templates/
│ │ ├── index.html # Home page with URL check form
│ │ ├── about.html # About project
│ │ ├── contact.html # Contact info
│ │ └── awareness.html # Phishing awareness and education
│ ├── init.py # Flask app init (optional)
│ ├── app.py # Main Flask application
│ ├── feature.py # URL feature extraction logic
│ └── Phishing URL Detection.ipynb # Model testing / debug notebook
├── ml_model/
│ ├── model.pkl # Trained scikit-learn model
│ ├── phishing.csv # Dataset used to train the model
│ └── Phishing URL Detection.ipynb # Training & evaluation notebook
├── requirements.txt # Python dependencies
├── runtime.txt # Python version for Render
├── Procfile # Deployment config for Render
├── venv/ # Local virtual environment (optional)
├── venv_phishnet/ # Alternate virtualenv (optional)

---

## 🛠️ Tech Stack

- Python 3.10
- Flask (Jinja2 templates)
- scikit-learn (ML model)
- Pandas & NumPy
- Bootstrap 5 (frontend UI)
- Gunicorn (production server)
- Render (cloud deployment)

---

## 🚀 Getting Started Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Pari0226/PhishNet.git
   cd PhishNet

   (Optional) Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app locally:

bash
Copy code
cd backend
python app.py
Visit http://127.0.0.1:5000 in your browser.

🔍 Model Details
Model: Gradient Boosting Classifier (from scikit-learn)

Features: 30 handcrafted lexical, domain-based & character features from the URL

Dataset: phishing.csv (included)

Training & testing handled in Phishing URL Detection.ipynb

Performance: ~97% accuracy on test set

📄 License
MIT License.
Feel free to use, fork, and contribute to this project.

🙋 Contact
Made with ❤️ by Pari Singh
📧 Email: singhpari94533@gmail.com
🔗 GitHub: Pari0226
