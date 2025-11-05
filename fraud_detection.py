import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_pipline.pkl")

st.title("Credit Card Fraud Detection App")

st.markdown("Please enter the transaction details and use the predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT"])
amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (receiver)", min_value=0.0, value=5000.0)
newbalanceDest = st.number_input("New Balance (receiver)", min_value=0.0, value=6000.0)
newbalanceDest = st.number_input("New Balance (receiver)", min_value=0.0, value=0.0)

if st.button("Predict Fraud"):
    input_data = pd.DataFrame({
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest]
    })

    prediction = model.predict(input_data)[0]

    st.subheader(f"prediction : '{int(prediction)}'")

    if prediction == 1:
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction looks like not fraud")