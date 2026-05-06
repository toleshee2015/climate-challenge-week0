import streamlit as st
import pandas as pd

st.title("Data Analysis Dashboard")

data = pd.read_csv("data/ethiopia.csv")  # ✅ relative path

st.write("Preview of dataset")
st.dataframe(data)