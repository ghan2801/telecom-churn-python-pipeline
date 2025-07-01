import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Load data from SQLite
engine = create_engine("sqlite:///processed_telecom_churn.db")
df = pd.read_sql("SELECT * FROM processed_churn", engine)

st.title("Telecom Churn Report")

st.subheader("Churn Distribution")
st.bar_chart(df["Churn"].value_counts())

st.subheader("Monthly Charges Distribution")
st.line_chart(df["MonthlyCharges"].sort_values())

st.subheader("Contract Type Breakdown")
st.write(df["ContractType"].value_counts())

st.subheader("Preview of Cleaned Data")
st.dataframe(df.head())
