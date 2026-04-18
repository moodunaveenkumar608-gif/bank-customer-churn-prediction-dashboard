from fastapi import FastAPI
import os
import joblib
import pandas as pd
import logging
from pydantic import BaseModel, Field, model_validator

app = FastAPI()

# Load trained model
MODEL_VERSION = "v1"
MODEL_PATH = f"models/churn_model_{MODEL_VERSION}.pkl"

model = joblib.load(MODEL_PATH)
# Configure logging
logging.basicConfig(
    filename="prediction_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


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

    @model_validator(mode="after")
    def validate_country(self):
        if self.country_Germany == 1 and self.country_Spain == 1:
            raise ValueError(
                "A customer cannot belong to both Germany and Spain."
            )
        return self


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

    not_churn_probability = float(probabilities[0])
    churn_probability = float(probabilities[1])

    if prediction == 1:
        result = "The customer is likely to churn"
        confidence = churn_probability
    else:
        result = "The customer is not likely to churn"
        confidence = not_churn_probability

    # Save text log
    logging.info(
        f"Input: {data.model_dump()} | "
        f"Prediction: {prediction} | "
        f"Not Churn Probability: {not_churn_probability:.4f} | "
        f"Churn Probability: {churn_probability:.4f}"
    )

    # Save prediction history to CSV
    history_row = pd.DataFrame([{
        "timestamp": pd.Timestamp.now(),
        "credit_score": data.credit_score,
        "age": data.age,
        "country_Germany": data.country_Germany,
        "country_Spain": data.country_Spain,
        "prediction": int(prediction),
        "churn_probability": round(churn_probability, 4)
    }])

    csv_path = os.path.join(
        os.path.dirname(__file__),
        "prediction_history.csv"
    )

    print("Saving file to:", csv_path)

    if os.path.exists(csv_path):
        history_row.to_csv(
            csv_path,
            mode="a",
            header=False,
            index=False
        )
    else:
        history_row.to_csv(
            csv_path,
            index=False
        )

    return {
    "prediction": int(prediction),
    "result": result,
    "confidence": round(confidence, 4),
    "not_churn_probability": round(not_churn_probability, 4),
    "churn_probability": round(churn_probability, 4),
    "model_version": MODEL_VERSION
}