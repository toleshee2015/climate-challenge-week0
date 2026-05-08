import streamlit as st
import pandas as pd
from pathlib import Path

# Title
st.title("Ethiopia Climate Analysis Dashboard")

# Load data
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "ethiopia.csv"

data = pd.read_csv(file_path)

# Success message
st.success("Data loaded successfully")

# Dataset shape
st.subheader("Dataset Shape")
st.write(data.shape)

# Preview
st.subheader("Dataset Preview")
st.dataframe(data.head())

# Column names
st.subheader("Column Names")
st.write(data.columns.tolist())

# Statistics
st.subheader("Statistics")
st.write(data.describe())

# Sidebar controls
st.sidebar.header("Controls")

numeric_columns = data.select_dtypes(include=['number']).columns.tolist()

selected_column = st.sidebar.selectbox(
    "Select a column",
    numeric_columns
)

chart_type = st.sidebar.radio(
    "Choose chart type",
    ["Line Chart", "Bar Chart", "Area Chart"]
)

# Visualization
st.subheader(f"{chart_type} for {selected_column}")

chart_data = data[[selected_column]]

if chart_type == "Line Chart":
    st.line_chart(chart_data)

elif chart_type == "Bar Chart":
    st.bar_chart(chart_data)

elif chart_type == "Area Chart":
    st.area_chart(chart_data)
