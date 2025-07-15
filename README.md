<<<<<<< HEAD
=======

>>>>>>> 96a3bb8 ( add readme)
# 🐟 PhishNet – AI‑Powered Phishing Detection Service

[![Build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)](#)
[![Python](https://img.shields.io/badge/python-3.10-blue?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-purple?style=flat-square)](#)

<<<<<<< HEAD
PhishNet is an AI-powered phishing detection web app that identifies malicious URLs using a trained machine learning model. It features a clean Flask-based interface, awareness content, and API endpoints for integration. Designed to be fast, educational, and deployment-ready.
=======
PhishNet is an AI-powered phishing detection web app that identifies malicious URLs using a trained machine learning model. It features a clean Flask-based interface styled with **Tailwind CSS**, awareness content, and API endpoints for integration. Designed to be fast, educational, and deployment-ready.
>>>>>>> 96a3bb8 ( add readme)

---

## 🌐 Live Demo

> Deployed via Render (free tier)  
<<<<<<< HEAD
> 🔗 https://phishnet.onrender.com *(link coming soon)*
=======
> 🔗 https://phishnet.onrender.com *(coming soon)*
>>>>>>> 96a3bb8 ( add readme)

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

<<<<<<< HEAD

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
=======
---

## 📁 Project Structure

```
PhishNet/
├── backend/
│   ├── static/
│   │   └── styles.css                # Custom Tailwind CSS styles
│   ├── templates/
│   │   ├── index.html               # Home page with phishing URL form
│   │   ├── about.html               # Project information
│   │   ├── contact.html             # Contact section
│   │   └── awareness.html           # Awareness & phishing education
│   ├── __init__.py                  # Flask app initializer (optional)
│   ├── app.py                       # Main Flask application
│   ├── feature.py                   # URL feature extraction logic
│   └── Phishing URL Detection.ipynb # Local experimentation / analysis
├── ml_model/
│   ├── model.pkl                    # Trained ML model (scikit-learn)
│   ├── phishing.csv                 # Dataset used for training
│   └── Phishing URL Detection.ipynb # Training notebook
├── requirements.txt                # Project dependencies
├── runtime.txt                     # Python version (for Render)
├── Procfile                        # Deployment command for Render
├── venv/                           # Optional local virtual environment
├── venv_phishnet/                  # Optional alternate venv (ignore in Git)
```
>>>>>>> 96a3bb8 ( add readme)

---

## 🛠️ Tech Stack

- Python 3.10
- Flask (Jinja2 templates)
<<<<<<< HEAD
- scikit-learn (ML model)
- Pandas & NumPy
- Bootstrap 5 (frontend UI)
- Gunicorn (production server)
- Render (cloud deployment)

---

## 🚀 Getting Started Locally
=======
- Tailwind CSS (UI styling)
- scikit-learn (Gradient Boosting Classifier)
- pandas, NumPy, requests
- Gunicorn (production WSGI server)
- Render.com (deployment)

---

## 🚀 Running Locally
>>>>>>> 96a3bb8 ( add readme)

1. Clone the repository:
   ```bash
   git clone https://github.com/Pari0226/PhishNet.git
   cd PhishNet
<<<<<<< HEAD

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
=======
   ```

2. Create & activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   cd backend
   python app.py
   ```

5. Open your browser at: http://localhost:5000

---

## 🔍 Model Details

- ✅ Model: Gradient Boosting Classifier (via scikit-learn)
- 📊 Features: Lexical patterns, URL structure, special characters, etc.
- 🗃 Dataset: Included `phishing.csv` (labeled malicious/legit)
- 🧪 Notebook: All training done in `Phishing URL Detection.ipynb`
- 🎯 Accuracy: ~97% on test set

---

## 🌍 Deployment (Render)

> Simple and free hosting via Render’s web service setup

1. Push to GitHub
2. Go to [https://render.com](https://render.com) → New Web Service
3. Connect your GitHub repo and configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn backend.app:app`
4. Files required:
   - `requirements.txt`
   - `Procfile`
   - `runtime.txt`
5. Deploy and you're live 🚀

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙋 Contact

Made with ❤️ by Pari Singh  
🔗 GitHub: [Pari0226](https://github.com/Pari0226)  
📧 Email: youremail@example.com  
>>>>>>> 96a3bb8 ( add readme)
