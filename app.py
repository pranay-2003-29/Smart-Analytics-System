import streamlit as st
import pandas as pd
import requests
from sqlalchemy import create_engine

st.title("📊 Smart Analytics – Customer Churn")

engine = create_engine(
    "postgresql://postgres:root@localhost:5432/smart_analytics"
)

df = pd.read_sql("SELECT * FROM churn_data", engine)

st.subheader("Customer Data")
st.dataframe(df.head())

st.subheader("Predict Customer Churn")

input_data = {}
for col in df.drop("Churn", axis=1).columns:
    input_data[col] = st.number_input(col, value=0.0)

if st.button("Predict"):
    response = requests.post(
        "http://localhost:5000/predict",
        json=input_data
    )
    result = response.json()
    st.success(f"Churn Probability: {result['churn_probability']}")
