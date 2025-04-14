# 📊 Telco Customer Churn Prediction App

This project uses machine learning to predict customer churn for a telecom company based on customer behavior and service usage data.

🧠 Built with:
- Logistic Regression & Random Forest
- Feature engineering & EDA in Python
- Streamlit for interactive deployment

---

## 📁 Project Structure


---

## 📊 Features Used
- Tenure
- Monthly & Total Charges
- Contract Type
- Internet Service
- Payment Method

All categorical features are one-hot encoded.

---

## 🚀 Streamlit App Demo

> 🎯 Use the interactive web app to test churn predictions based on input values.

📍 **Live App**  
🌐 [https://yourapp.streamlit.app](https://telco-churn-ml-app-m3veta6rrgkwmiqdgwekap.streamlit.app)

---

## 🧠 ML Models Used

- **Logistic Regression** (baseline)
- **Random Forest** (primary model)
- Evaluated using Accuracy, Confusion Matrix, and Feature Importance

---

## 📌 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/kwamearhinPORTFL/telco-churn-ml-app.git
cd telco-churn-ml-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
