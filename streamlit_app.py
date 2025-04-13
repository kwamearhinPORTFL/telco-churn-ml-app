import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("rf_model.pkl")

st.title("📊 Telco Customer Churn Predictor")

st.markdown("Enter customer details below:")

# Simple features for now
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.slider("Monthly Charges", 0.0, 150.0, 70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=500.0)

# Contract type (one-hot encoding)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
contract_one_year = 1 if contract == "One year" else 0
contract_two_year = 1 if contract == "Two year" else 0

# Internet Service
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
internet_fiber = 1 if internet == "Fiber optic" else 0
internet_no = 1 if internet == "No" else 0

# Payment Method
payment = st.selectbox("Payment Method", [
    "Electronic check", 
    "Mailed check", 
    "Bank transfer (automatic)", 
    "Credit card (automatic)"
])
payment_bank = 1 if payment == "Bank transfer (automatic)" else 0
payment_credit = 1 if payment == "Credit card (automatic)" else 0
payment_mailed = 1 if payment == "Mailed check" else 0

# Create feature input array
input_data = np.array([[tenure, monthly_charges, total_charges,
                        contract_one_year, contract_two_year,
                        internet_fiber, internet_no,
                        payment_bank, payment_credit, payment_mailed]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    result = "❌ Customer will churn" if prediction == 1 else "✅ Customer will stay"
    st.success(f"Prediction: {result}")
