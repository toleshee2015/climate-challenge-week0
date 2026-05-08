import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Climate Dashboard")

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "ethiopia.csv"

data = pd.read_csv(file_path)

st.success("Data loaded successfully")

st.write("Dataset shape:", data.shape)

st.subheader("Dataset Preview")
st.dataframe(data.head())

st.subheader("Column Names")
st.write(data.columns.tolist())

st.subheader("Statistics")
st.write(data.describe())
