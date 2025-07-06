# 📧 Email Spam Detection API

This project is a Flask-based REST API for detecting spam emails using a Machine Learning model.

## 🚀 Features

- `/train` → Trains the spam detection model
- `/predict` → Predicts if a given email is spam or not
- `/best_model_parameter` → Returns the best hyperparameters used

## 🛠️ Requirements

- Python 3.8+
- Flask
- Scikit-learn
- Pandas
- MLflow (for experiment tracking)

## ⚙️ Setup Instructions

1. **Clone the Repository**
```bash
git clone git@github.com:your-username/email-spam-detection.git
cd email-spam-detection
