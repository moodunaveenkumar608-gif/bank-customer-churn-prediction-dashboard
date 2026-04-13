from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("churn_model.pkl")


class CustomerData(BaseModel):
    credit_score: int = Field(..., ge=300, le=900)
    age: int = Field(..., ge=18, le=100)
    tenure: int = Field(..., ge=0, le=50)
    balance: float = Field(..., ge=0)
    products_number: int = Field(..., ge=1, le=10)
    credit_card: int = Field(..., ge=0, le=1)
    active_member: int = Field(..., ge=0, le=1)
    estimated_salary: float = Field(..., ge=0)
    country_Germany: int = Field(..., ge=0, le=1)
    country_Spain: int = Field(..., ge=0, le=1)
    gender_Male: int = Field(..., ge=0, le=1)


@app.get("/")
def home():
    return {"message": "Bank Customer Churn Prediction API is running"}


@app.post("/predict")
def predict(data: CustomerData):
    sample = pd.DataFrame([{
        "credit_score": data.credit_score,
        "age": data.age,
        "tenure": data.tenure,
        "balance": data.balance,
        "products_number": data.products_number,
        "credit_card": data.credit_card,
        "active_member": data.active_member,
        "estimated_salary": data.estimated_salary,
        "country_Germany": data.country_Germany,
        "country_Spain": data.country_Spain,
        "gender_Male": data.gender_Male
    }])

    prediction = model.predict(sample)[0]
    probabilities = model.predict_proba(sample)[0]

    not_churn_confidence = float(probabilities[0])
    churn_confidence = float(probabilities[1])

    if prediction == 1:
        result = "The customer is likely to churn"
        confidence = churn_confidence
    else:
        result = "The customer is not likely to churn"
        confidence = not_churn_confidence

    return {
        "prediction": int(prediction),
        "result": result,
        "confidence": round(confidence, 4),
        "not_churn_probability": round(not_churn_confidence, 4),
        "churn_probability": round(churn_confidence, 4)
    }