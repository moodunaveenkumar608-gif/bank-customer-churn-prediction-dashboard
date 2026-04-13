import joblib
import pandas as pd

# Load the saved model
model = joblib.load("churn_model.pkl")
print("Model loaded successfully")

# Create sample input with exact feature names
sample = pd.DataFrame([{
    'credit_score': 600,
    'age': 40,
    'tenure': 3,
    'balance': 60000,
    'products_number': 2,
    'credit_card': 1,
    'active_member': 1,
    'estimated_salary': 50000,
    'country_Germany': 1,
    'country_Spain': 0,
    'gender_Male': 1
}])

# Predict
prediction = model.predict(sample)

print("Prediction:", prediction)