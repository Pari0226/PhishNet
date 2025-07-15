# 🐟 PhishNet &nbsp;– AI‑powered Phishing‑Detection Service

[![Build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)](#)
[![Python](https://img.shields.io/badge/python-3.10-blue?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-purple?style=flat-square)](#)

An end‑to‑end phishing‑detection platform that uses classical ML to spot malicious URLs and e‑mails in real‑time.  
Deployable as a **Flask + REST API** or via a **one‑click Render button**.

---

## 🌐 Live Demo

> **URL** <https://phishnet.onrender.com> &nbsp;*(deployed on Render free tier)*  

Try pasting a URL in the demo – PhishNet will predict the probability of it being **safe** vs **phishing** and show the full feature vector it extracted.

<p align="center">
  <img src="docs/screenshot_url_check.png" width="450">
</p>

---

## ✨ Key Features

| Category | Details |
|----------|---------|
| 🔗 **URL model** | 30 handcrafted lexical & host‑based features → Gradient Boosting Classifier |
| 📧 **E‑mail model** | TF‑IDF + Logistic Regression *(optional, disable if not needed)* |
| ⚡ **Fast API** | `/predict‑url` and `/predict‑email` JSON endpoints (0.5 ms avg) |
| 🖥️ **Flask UI** | Clean Bootstrap 5 interface for non‑technical users |
| 🛡️ **Stateless** | No DB required; model is loaded once at startup |
| 🚀 **1‑click Deploy** | Works on Render free tier (or Docker) with a 40 MB container |

---

## 🛠 Tech Stack

* **Python 3.10**   •   Flask & Jinja 2   •   scikit‑learn 1.3  
* Pandas | NumPy | Requests | BeautifulSoup *(URL scraping)*  
* Gunicorn for production serving  
* **Render** for cloud hosting (Heroku‑style buildpacks)

---

## 📁 Folder Structure

