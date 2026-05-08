import streamlit as st
import pandas as pd
from pathlib import Path

st.title("My Dashboard")

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "ethiopia.csv"

data = pd.read_csv(file_path)

st.write("Data loaded successfully")
st.dataframe(data)
