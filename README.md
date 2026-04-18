# 🏦 Bank Customer Churn Prediction Dashboard

An end-to-end machine learning project that predicts whether a bank customer is likely to leave the bank.

This project includes:

* a **Streamlit frontend**
* a **FastAPI backend**
* a trained **Random Forest Classifier**
* **Dockerized setup**
* **CI pipeline with GitHub Actions**
* deployed services using **Streamlit Community Cloud** and **Render**

---

## 🚀 Live Demo

### Streamlit App

[Bank Customer Churn Prediction Dashboard](https://bank-customer-churn-prediction-dashboard-bzt4hqmo7zwymfzq5awat.streamlit.app/)

### FastAPI Documentation

[FastAPI Swagger Docs](https://bank-customer-churn-prediction-dashboard.onrender.com/docs)

### GitHub Repository

[GitHub Repository](https://github.com/moodunaveenkumar608-gif/bank-customer-churn-prediction-dashboard)

---

## 📌 Project Overview

Customer churn is one of the biggest challenges for banks. This project predicts whether a customer is likely to leave the bank based on customer details such as:

* Credit score
* Age
* Tenure
* Balance
* Number of products
* Geography
* Gender
* Estimated salary
* Credit card ownership
* Active membership status

The application returns:

* churn prediction
* churn probability
* risk level (**Low / Medium / High**)

---

## 🛠️ Technologies Used

* Python
* Streamlit
* FastAPI
* Scikit-learn
* Pandas
* Plotly
* Joblib
* Requests
* Docker
* GitHub Actions
* Render
* Streamlit Community Cloud

---

## 🧠 Machine Learning Model

* **Model Used:** Random Forest Classifier
* **Target Variable:** Customer Churn
* **Saved Model Format:** `churn_model.pkl`

Prediction output:

* `0` → Customer is likely to stay
* `1` → Customer is likely to leave

---

## ✨ Features

* Predict customer churn in real time
* Display churn probability
* Show risk level using a gauge chart
* Store prediction history in CSV format
* Download prediction history
* Visualize prediction history in a dashboard
* FastAPI backend with request validation
* Error handling when backend is unavailable
* Live integration between Streamlit and FastAPI
* Logging and monitoring support

---

## ⚙️ MLOps Features

* API-based prediction service
* Input validation with Pydantic
* Dockerized application
* Prediction logging
* Prediction history tracking
* Monitoring dashboard
* Continuous Integration (CI) using GitHub Actions

---

## 🏗️ Project Architecture

```text
User → Streamlit Frontend → FastAPI Backend → ML Model → Logs + Prediction History → Monitoring Dashboard
```

---

## 📂 Project Structure

```text
Bank_Churn_Prediction/
│
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI pipeline
├── models/                     # Model-related files
├── app.py                      # Streamlit frontend
├── main.py                     # FastAPI backend
├── churn_model.pkl             # Trained ML model
├── Dockerfile                  # Docker image configuration
├── docker-compose.yml          # Multi-container setup
├── requirements.txt            # Required libraries
├── test_model.py               # Model/API test file
├── README.md                   # Project documentation
├── .gitignore
└── .dockerignore
```

---

## ⚙️ Installation and Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/moodunaveenkumar608-gif/bank-customer-churn-prediction-dashboard.git
cd bank-customer-churn-prediction-dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Backend

```bash
uvicorn main:app --reload
```

FastAPI will run at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### 4. Run Streamlit Frontend

Open another terminal and run:

```bash
streamlit run app.py
```

Streamlit will run at:

```text
http://localhost:8501
```

---

## 🐳 Run with Docker

```bash
docker compose up --build
```

Services:

* Streamlit → `http://localhost:8501`
* FastAPI Docs → `http://localhost:8000/docs`

---

## 🔗 API Endpoint

### POST `/predict`

Example request:

```json
{
  "credit_score": 740,
  "age": 40,
  "tenure": 10,
  "balance": 60000,
  "products_number": 2,
  "credit_card": 1,
  "active_member": 1,
  "estimated_salary": 50000,
  "country_Germany": 1,
  "country_Spain": 0,
  "gender_Male": 1
}
```

Example response:

```json
{
  "prediction": 0,
  "result": "The customer is not likely to churn",
  "confidence": 0.61,
  "not_churn_probability": 0.61,
  "churn_probability": 0.39,
  "model_version": "v1"
}
```

---

## ✅ CI Pipeline

This project includes a GitHub Actions CI workflow that automatically:

* checks repository files
* installs dependencies
* validates Python syntax
* builds Docker services

This helps ensure the project remains stable whenever code is pushed to GitHub.

---

## 📈 Future Improvements

* Add automated tests for API endpoints
* Store prediction history in a database
* Add user authentication
* Improve model performance with hyperparameter tuning
* Add Continuous Deployment (CD)
* Deploy a fully containerized version to cloud platforms such as AWS, Azure, or Railway

---

## 👨‍💻 Author

**Moodu Naveenkumar**
Aspiring Data Scientist passionate about Machine Learning, FastAPI, Streamlit, Docker, and building real-world projects.

---

## ⭐ Support

If you found this project useful, please give it a star on GitHub.
