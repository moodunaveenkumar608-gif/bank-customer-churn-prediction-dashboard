# 🏦 Bank Customer Churn Prediction Dashboard

An end-to-end machine learning project that predicts whether a bank customer is likely to leave the bank.

This project includes:

* A frontend built with Streamlit
* A backend API built with FastAPI
* A trained Random Forest machine learning model
* Live deployment using Streamlit Community Cloud and Render

---

# 🚀 Live Demo

### Streamlit App

[https://bank-customer-churn-prediction-dashboard-bzt4hqmo7zwymfzq5awat.streamlit.app/](https://bank-customer-churn-prediction-dashboard-bzt4hqmo7zwymfzq5awat.streamlit.app/)

### FastAPI Documentation

[https://bank-customer-churn-prediction-dashboard.onrender.com/docs](https://bank-customer-churn-prediction-dashboard.onrender.com/docs)

### GitHub Repository

[https://github.com/moodunaveenkumar608-gif/bank-customer-churn-prediction-dashboard](https://github.com/moodunaveenkumar608-gif/bank-customer-churn-prediction-dashboard)

---

# 📌 Project Overview

Customer churn is one of the biggest challenges for banks. This project predicts whether a customer is likely to leave the bank based on factors such as:

* Credit score
* Age
* Balance
* Number of products
* Geography
* Gender
* Estimated salary
* Active membership status

The model returns:

* Churn prediction
* Churn probability
* Risk level (Low / Medium / High)

---

# 🛠️ Technologies Used

* Python
* Streamlit
* FastAPI
* Scikit-learn
* Pandas
* Plotly
* Joblib
* Requests
* Render
* Streamlit Community Cloud

---

# 🧠 Machine Learning Model

* Model Used: Random Forest Classifier
* Target Variable: Customer Churn
* Saved Model Format: `churn_model.pkl`

The model predicts:

* `0` → Customer is likely to stay
* `1` → Customer is likely to leave

---

# ✨ Features

* Predict customer churn
* Display churn probability
* Show risk level using a gauge chart
* Store prediction history in CSV format
* Download prediction history
* Beautiful Streamlit dashboard
* FastAPI backend with validation
* Error handling when backend is unavailable
* Live API integration between Streamlit and FastAPI
* Input validation using Pydantic
FastAPI backend for prediction API
Live API deployment on Render
Prediction logging
Prediction history saved to CSV
Monitoring dashboard in Streamlit


## MLOps Features

API-based prediction service

Input validation

Logging to text file

Prediction history tracking

Monitoring dashboard

Frontend and backend deployment

---

# 🏗️ Project Architecture

```text
User → Streamlit Frontend → FastAPI Backend → ML Model → Logs + Prediction History → Monitoring Dashboard
```

---

# 📂 Project Structure

```text
Bank_Churn_Prediction/
│
├── app.py                  # Streamlit frontend
├── main.py                 # FastAPI backend
├── churn_model.pkl         # Trained ML model
├── requirements.txt        # Required libraries
├── history.csv             # Saved prediction history
├── README.md               # Project documentation
├── Dockerfile              # Docker configuration (future deployment)
└── test_model.py           # Model testing script
```

---

# ⚙️ Installation and Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/moodunaveenkumar608-gif/bank-customer-churn-prediction-dashboard.git
cd bank-customer-churn-prediction-dashboard
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run FastAPI Backend

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

## 4. Run Streamlit Frontend

Open another terminal and run:

```bash
streamlit run app.py
```

Streamlit will run at:

```text
http://localhost:8501
```

---

# 🔗 API Endpoint

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
  "churn_probability": 0.39
}

---

# 📈 Future Improvements

* Docker deployment
* User authentication
* Database integration
* Cloud deployment with AWS or Azure
* CI/CD pipeline
* Improved model performance

---

# 👨‍💻 Author

Moodu Naveenkumar

Aspiring Data Scientist passionate about Machine Learning, FastAPI, Streamlit, and building real-world projects.

---

# ⭐ If You Like This Project

If you found this project useful, please give the repository a star on GitHub!

