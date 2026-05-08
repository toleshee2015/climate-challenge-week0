import streamlit as st
import pandas as pd

st.title("Data Analysis Dashboard")

# data
data = pd.read_csv(r"C:\Users\Soret\climate-challenge-week0\data\ethiopia.csv")

st.write("Preview of dataset")
st.dataframe(data)