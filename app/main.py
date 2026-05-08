import streamlit as st
import pandas as pd
from pathlib import Path

st.title("🌍 Africa Climate Dashboard")

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "data" / "ethiopia.csv"

data = pd.read_csv(file_path)

st.success("Data loaded successfully")

st.sidebar.header("🌍 Country Comparison")

countries = data["country"].unique()

selected_countries = st.sidebar.multiselect(
    "Select countries",
    countries,
    default=list(countries[:2])
)

filtered = data[data["country"].isin(selected_countries)]
