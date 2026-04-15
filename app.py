import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import os
import requests

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Bank Customer Churn Prediction",
    page_icon="🏦",
    layout="wide"
)

# -----------------------------------
# Custom CSS Styling
# -----------------------------------
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #0E3B5F;
    margin-bottom: 5px;
}
.sub-title {
    font-size: 18px;
    color: #4F5D75;
    margin-bottom: 20px;
}
.section-title {
    font-size: 26px;
    font-weight: 600;
    color: #12344D;
    margin-top: 20px;
    margin-bottom: 10px;
}
.kpi-card {
    background-color: #F7F9FC;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    text-align: center;
}
.kpi-value {
    font-size: 28px;
    font-weight: bold;
    color: #0E3B5F;
}
.kpi-label {
    font-size: 16px;
    color: #5C6B7A;
}
.footer-text {
    text-align: center;
    color: #6c757d;
    font-size: 14px;
    padding-top: 20px;
    padding-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# Header Image
# -----------------------------------
if os.path.exists("bank.jpg"):
    image = Image.open("bank.jpg")
    st.image(image, use_container_width=True)

# -----------------------------------
# Header
# -----------------------------------
st.markdown('<div class="main-title">🏦 Bank Customer Churn Prediction Dashboard</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Predict whether a customer is likely to leave the bank using a machine learning model, visualize churn risk, and track prediction history.</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------------
# Sidebar
# -----------------------------------
st.sidebar.title("Navigation Panel")
st.sidebar.info(
    "This application predicts customer churn based on customer account and demographic details."
)
st.sidebar.markdown("### Project Highlights")
st.sidebar.write("✅ Real-time prediction")
st.sidebar.write("✅ Churn probability")
st.sidebar.write("✅ Risk visualization")
st.sidebar.write("✅ Dashboard and history")

# -----------------------------------
# Input Section
# -----------------------------------
st.markdown('<div class="section-title">Customer Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    tenure = st.number_input("Tenure", min_value=0, max_value=10, value=5)
    balance = st.number_input("Balance", min_value=0.0, value=50000.0)
    estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

with col2:
    num_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
    has_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
    is_active = st.selectbox("Is Active Member?", ["Yes", "No"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

# -----------------------------------
# Prediction Button
# -----------------------------------
if st.button("🔍 Predict Churn", use_container_width=True):

    data = {
        "credit_score": int(credit_score),
        "age": int(age),
        "tenure": int(tenure),
        "balance": float(balance),
        "products_number": int(num_products),
        "credit_card": 1 if has_card == "Yes" else 0,
        "active_member": 1 if is_active == "Yes" else 0,
        "estimated_salary": float(estimated_salary),
        "country_Germany": 1 if geography == "Germany" else 0,
        "country_Spain": 1 if geography == "Spain" else 0,
        "gender_Male": 1 if gender == "Male" else 0
    }

    try:
        response = requests.post(
            "https://bank-customer-churn-prediction-dashboard.onrender.com/predict",
             json=data
        )

        if response.status_code == 200:
            result = response.json()

            prediction = result["prediction"]
            probability = result["churn_probability"]

        else:
            st.error("Prediction failed. Please check the FastAPI server.")
            st.stop()

    except requests.exceptions.ConnectionError:
        st.error("FastAPI server is not running. Please start FastAPI first.")
        st.stop()
    st.markdown("---")
    st.markdown('<div class="section-title">Prediction Result</div>', unsafe_allow_html=True)

    result_col1, result_col2 = st.columns([1, 1])

    with result_col1:
        if prediction == 1:
            st.error("⚠️ This customer is likely to leave the bank.")
            risk_level = "High"
        else:
            st.success("✅ This customer is likely to stay with the bank.")
            risk_level = "Low"

        st.markdown(f"### Churn Probability: **{probability:.2%}**")
        if probability < 0.40:
            st.info("Risk Level: Low")
            risk_level = "Low"
        elif probability < 0.70:
            st.warning("Risk Level: Medium")
            risk_level = "Medium"
        else:
            st.error("Risk Level: High")
            risk_level = "High"

    with result_col2:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability * 100,
            title={"text": "Churn Risk (%)"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#12344D"},
                "steps": [
                    {"range": [0, 40], "color": "#B7E4C7"},
                    {"range": [40, 70], "color": "#FFE8A1"},
                    {"range": [70, 100], "color": "#F4A6A6"}
                ]
            }
        ))
        fig.update_layout(height=330)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.markdown('<div class="section-title">Customer Input Summary</div>', unsafe_allow_html=True)

    summary_df = pd.DataFrame({
        "Feature": [
            "Credit Score", "Age", "Tenure", "Balance", "Estimated Salary",
            "Number of Products", "Has Credit Card", "Is Active Member",
            "Gender", "Geography"
        ],
        "Value": [
            credit_score, age, tenure, balance, estimated_salary,
            num_products, has_card, is_active, gender, geography
        ]
    })

    st.dataframe(summary_df, use_container_width=True)

    history_row = pd.DataFrame([{
        "CreditScore": credit_score,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "EstimatedSalary": estimated_salary,
        "NumProducts": num_products,
        "HasCard": has_card,
        "IsActive": is_active,
        "Gender": gender,
        "Geography": geography,
        "Prediction": "Leave" if prediction == 1 else "Stay",
        "Probability": float(probability * 100),
        "RiskLevel": risk_level
    }])

    if os.path.exists("history.csv"):
        history_row.to_csv("history.csv", mode="a", header=False, index=False)
    else:
        history_row.to_csv("history.csv", index=False)

# -----------------------------------
# Dashboard Section
# -----------------------------------
st.markdown("---")
st.markdown('<div class="section-title">Prediction Dashboard</div>', unsafe_allow_html=True)

if os.path.exists("history.csv"):
    history = pd.read_csv("history.csv")

    if not history.empty:
        total_predictions = len(history)
        stay_count = (history["Prediction"] == "Stay").sum() if "Prediction" in history.columns else 0
        leave_count = (history["Prediction"] == "Leave").sum() if "Prediction" in history.columns else 0

        kpi1, kpi2, kpi3 = st.columns(3)

        with kpi1:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{total_predictions}</div>
                <div class="kpi-label">Total Predictions</div>
            </div>
            """, unsafe_allow_html=True)

        with kpi2:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{stay_count}</div>
                <div class="kpi-label">Likely to Stay</div>
            </div>
            """, unsafe_allow_html=True)

        with kpi3:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-value">{leave_count}</div>
                <div class="kpi-label">Likely to Leave</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            if "Prediction" in history.columns:
                pred_counts = history["Prediction"].value_counts().reset_index()
                pred_counts.columns = ["Prediction", "Count"]
                pie_fig = px.pie(
                    pred_counts,
                    names="Prediction",
                    values="Count",
                    title="Prediction Distribution",
                    hole=0.4
                )
                st.plotly_chart(pie_fig, use_container_width=True)

        with chart_col2:
            if "Geography" in history.columns:
                geo_counts = history["Geography"].value_counts().reset_index()
                geo_counts.columns = ["Geography", "Count"]
                bar_fig = px.bar(
                    geo_counts,
                    x="Geography",
                    y="Count",
                    title="Predictions by Geography",
                    text_auto=True
                )
                st.plotly_chart(bar_fig, use_container_width=True)

        if "Age" in history.columns:
            hist_fig = px.histogram(
                history,
                x="Age",
                nbins=20,
                title="Age Distribution of Predicted Customers"
            )
            st.plotly_chart(hist_fig, use_container_width=True)

        st.markdown('<div class="section-title">Prediction History</div>', unsafe_allow_html=True)
        st.dataframe(history, use_container_width=True)

        csv = history.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇ Download Prediction History",
            data=csv,
            file_name="prediction_history.csv",
            mime="text/csv",
            use_container_width=True
        )
    else:
        st.info("No prediction history yet. Make your first prediction above.")
else:
    st.info("No prediction history yet. Make your first prediction above.")
st.markdown("---")
st.markdown("## Model Monitoring Dashboard")

try:
    history_df = pd.read_csv("prediction_history.csv")

    total_predictions = len(history_df)
    avg_churn_probability = history_df["churn_probability"].mean()
    churn_count = (history_df["prediction"] == 1).sum()
    not_churn_count = (history_df["prediction"] == 0).sum()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Predictions", total_predictions)

    with col2:
        st.metric("Average Churn Probability", f"{avg_churn_probability:.2%}")

    with col3:
        st.metric("Likely to Churn", churn_count)

    st.markdown("### Last 10 Predictions")
    st.dataframe(history_df.tail(10), use_container_width=True)

    st.markdown("### Prediction Distribution")
    prediction_counts = history_df["prediction"].value_counts().sort_index()
    st.bar_chart(prediction_counts)

except FileNotFoundError:
    st.info("No prediction history available yet.")

st.markdown("### Churn Probability Trend")

history_df["timestamp"] = pd.to_datetime(history_df["timestamp"])

trend_data = history_df[["timestamp", "churn_probability"]]

st.line_chart(
    trend_data.set_index("timestamp")
)

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")

st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 15px; padding-top: 10px;'>
        Built with Python, Streamlit, Scikit-learn, Plotly, and passion for Data Science.<br><br>
        Created by <b>Moodu Naveenkumar</b>
    </div>
    """,
    unsafe_allow_html=True
)
