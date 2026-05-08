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
st.title("🌍 Africa Climate Dashboard")

st.markdown("""
This dashboard provides interactive climate analysis across African countries.

You can:
- explore dataset by country
- compare climate variables
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
# Sidebar - Country Comparison
# -----------------------------
st.sidebar.header("🌍 Country Comparison")

if "country" in data.columns:
    countries = sorted(data["country"].unique())

    selected_countries = st.sidebar.multiselect(
        "Select countries",
        countries,
        default=countries[:2] if len(countries) >= 2 else countries
    )

    filtered_data = data[data["country"].isin(selected_countries)]
else:
    st.warning("No 'country' column found. Showing single-country data.")
    filtered_data = data

# -----------------------------
# Sidebar - Variable Selection
# -----------------------------
st.sidebar.header("⚙ Dashboard Controls")

numeric_columns = filtered_data.select_dtypes(include=['number']).columns.tolist()

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

col1.metric("Rows", filtered_data.shape[0])
col2.metric("Columns", filtered_data.shape[1])
col3.metric(
    "Average",
    round(filtered_data[selected_column].mean(), 2)
)

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("📁 Dataset Preview")

st.dataframe(
    filtered_data.head(num_rows),
    use_container_width=True
)

# -----------------------------
# Country Comparison Chart
# -----------------------------
if "country" in filtered_data.columns:
    st.subheader(f"🌍 Country Comparison: {selected_column}")

    comparison_chart = filtered_data.pivot_table(
        index="year" if "year" in filtered_data.columns else filtered_data.index,
        columns="country",
        values=selected_column
    )

    st.line_chart(comparison_chart)

# -----------------------------
# Single Variable Visualization
# -----------------------------
st.subheader(f"📈 {chart_type}: {selected_column}")

chart_data = filtered_data[[selected_column]]

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

st.dataframe(filtered_data.describe(), use_container_width=True)

# -----------------------------
# Data Description
# -----------------------------
st.subheader("ℹ Dataset Description")

st.info("""
This dashboard supports multi-country climate comparison across Africa.
Users can select countries and analyze temperature, rainfall,
and other environmental indicators interactively.
""")
