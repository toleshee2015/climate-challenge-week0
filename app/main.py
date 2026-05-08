# =============================
# 1. IMPORTS
# =============================
import streamlit as st
import pandas as pd
from pathlib import Path
# =============================
# 2. PAGE CONFIGURATION
# =============================
st.set_page_config(
    page_title="Africa Climate Dashboard",
    page_icon="🌍",
    layout="wide"
)
# =============================
# 3. CUSTOM STYLING
# =============================
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

# =============================
# 4. TITLE + DESCRIPTION
# =============================
st.title("🌍 Africa Climate Dashboard")

st.markdown("""
This dashboard allows interactive exploration of climate data across African countries.

Users can:
- Select countries
- Compare climate indicators
- Visualize trends
- View statistics
""")
# =============================
# 5. LOAD DATA
# =============================
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "ethiopia.csv"

data = pd.read_csv(file_path)
# =============================
# 6. COUNTRY FLAGS
# =============================
country_flags = {
    "Ethiopia": "🇪🇹",
    "Kenya": "🇰🇪",
    "Nigeria": "🇳🇬",
    "Tanzania": "🇹🇿",
    "Sudan": "🇸🇩",
    "Uganda": "🇺🇬",
}
# =============================
# 7. DATA OVERVIEW
# =============================
st.subheader("📌 Dataset Overview")

if "country" in data.columns:
    st.markdown("### 🌍 Available Countries")
    st.write(sorted(data["country"].unique()))

st.markdown("### 📊 Available Indicators")
st.write(data.select_dtypes(include=["number"]).columns.tolist())
# =============================
# 8. SIDEBAR - COUNTRY SELECTION
# =============================
st.sidebar.header("🌍 Country Comparison")

if "country" in data.columns:
    countries = sorted(data["country"].unique())

    country_options = [
        f"{country_flags.get(c, '🌍')} {c}" for c in countries
    ]

    selected_display = st.sidebar.multiselect(
        "Select countries",
        country_options,
        default=country_options[:2] if len(country_options) >= 2 else country_options
    )

    selected_countries = [
        c.split(" ", 1)[1] for c in selected_display
    ]

    filtered_data = data[data["country"].isin(selected_countries)]
else:
    filtered_data = data

# =============================
# 9. SIDEBAR - INDICATOR
# =============================
st.sidebar.header("📊 Indicator Selection")

numeric_columns = filtered_data.select_dtypes(include=["number"]).columns.tolist()

selected_column = st.sidebar.selectbox(
    "Select variable",
    numeric_columns
)

chart_type = st.sidebar.selectbox(
    "Chart type",
    ["Line Chart", "Bar Chart", "Area Chart"]
)
# =============================
# 10. METRICS
# =============================
st.subheader("📊 Quick Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", filtered_data.shape[0])
col2.metric("Columns", filtered_data.shape[1])
col3.metric("Average", round(filtered_data[selected_column].mean(), 2))
# =============================
# 11. DATA PREVIEW
# =============================
st.subheader("📁 Dataset Preview")

display_data = filtered_data.copy()

if "country" in display_data.columns:
    display_data["country"] = display_data["country"].apply(
        lambda x: f"{country_flags.get(x, '🌍')} {x}"
    )

st.dataframe(display_data.head(10))
# =============================
# 12. COUNTRY COMPARISON CHART
# =============================
if "country" in filtered_data.columns:
    st.subheader(f"🌍 Country Comparison: {selected_column}")

    comparison = filtered_data.pivot_table(
        index="year" if "year" in filtered_data.columns else filtered_data.index,
        columns="country",
        values=selected_column
    )

    st.line_chart(comparison)
    # =============================
# 13. SINGLE VARIABLE CHART
# =============================
st.subheader(f"📈 {chart_type}: {selected_column}")

chart_data = filtered_data[[selected_column]]

if chart_type == "Line Chart":
    st.line_chart(chart_data)

elif chart_type == "Bar Chart":
    st.bar_chart(chart_data)

elif chart_type == "Area Chart":
    st.area_chart(chart_data)
    # =============================
# 14. STATISTICS
# =============================
st.subheader("📌 Statistical Summary")

st.dataframe(filtered_data.describe())
# =============================
# 15. FOOTER DESCRIPTION
# =============================
st.info("""
This dashboard provides comparative climate analysis across African countries.

It supports:
- Country selection with flags
- Climate variable analysis
- Time-series comparison
- Interactive visualization
""")
