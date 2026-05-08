import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "ethiopia.csv"

data = pd.read_csv(file_path)

import streamlit as st

st.title("My Dashboard")
st.write("If you see this, Streamlit works")
