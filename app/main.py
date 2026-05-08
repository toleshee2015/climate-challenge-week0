from pathlib import Path
import pandas as pd
import streamlit as st

st.title("Climate Dashboard")

# Go one level up from app/ to project root
BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "data" / "ethiopia.csv"

data = pd.read_csv(file_path)

st.success("Data loaded successfully")
st.dataframe(data.head())
