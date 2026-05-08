import streamlit as st
import pandas as pd
from pathlib import Path

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Climate Dashboard",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }

    h1 {
        color: #1f77b4;
    }

    .stMetric {
        background-color: white;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Title and Description
# -----------------------------
st.title("🌍 Ethiopia Climate Dashboard")

st.markdown("""
This dashboard provides interactive climate analysis for Ethiopia.

You can:
- explore the dataset
- filter climate variables
- visualize trends
- inspect statistics interactively
""")

# -----------------------------
# Load Dataset
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "ethiopia.csv"

data = pd.read_csv(file_path)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("⚙ Dashboard Controls")

numeric_columns = data.select_dtypes(include=['number']).columns.tolist()

selected_column = st.sidebar.selectbox(
    "Select climate variable",
    numeric_columns
)

chart_type = st.sidebar.selectbox(
    "Select chart type",
    ["Line Chart", "Bar Chart", "Area Chart"]
)

num_rows = st.sidebar.slider(
    "Rows to display",
    5,
    50,
    10
)

# -----------------------------
# Metrics Section
# -----------------------------
st.subheader("📊 Quick Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", data.shape[0])
col2.metric("Columns", data.shape[1])
col3.metric(
    "Average",
    round(data[selected_column].mean(), 2)
)

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("📁 Dataset Preview")

st.dataframe(
    data.head(num_rows),
    use_container_width=True
)

# -----------------------------
# Visualization
# -----------------------------
st.subheader(f"📈 {chart_type}: {selected_column}")

chart_data = data[[selected_column]]

if chart_type == "Line Chart":
    st.line_chart(chart_data)

elif chart_type == "Bar Chart":
    st.bar_chart(chart_data)

elif chart_type == "Area Chart":
    st.area_chart(chart_data)

# -----------------------------
# Statistics
# -----------------------------
st.subheader("📌 Statistical Summary")

st.dataframe(data.describe(), use_container_width=True)

# -----------------------------
# Data Description
# -----------------------------
st.subheader("ℹ Dataset Description")

st.info("""
This dataset contains climate-related observations for Ethiopia.
The dashboard allows exploration of temperature, rainfall,
and other environmental indicators interactively.
""")
