from pathlib import Path
import pandas as pd
import streamlit as st

st.title("🌍 Africa Climate Dashboard")

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "ethiopia.csv"

data = pd.read_csv(file_path)
st.sidebar.header("🌍 Country Comparison")

countries = sorted(data["country"].unique())

selected_countries = st.sidebar.multiselect(
    "Select countries to compare",
    countries,
    default=countries[:2] if len(countries) >= 2 else countries
)
filtered_data = data[data["country"].isin(selected_countries)]

st.sidebar.header("📊 Indicator")

indicator = st.sidebar.selectbox(
    "Select variable",
    ["temperature", "rainfall"]
)

st.subheader("📈 Country Comparison Over Time")

comparison = filtered_data.pivot_table(
    index="year",
    columns="country",
    values=indicator
)

st.line_chart(comparison)
latest_year = filtered_data["year"].max()

latest_data = filtered_data[filtered_data["year"] == latest_year]

st.subheader(f"📊 {latest_year} Snapshot Comparison")

st.subheader("📁 Filtered Data")

st.dataframe(filtered_data)
st.bar_chart(latest_data.set_index("country")[indicator])

st.subheader("📁 Filtered Data")

st.dataframe(filtered_data)
mode = st.radio(
    "Analysis Mode",
    ["Single Country", "Africa Comparison"]
)
if mode == "Single Country":
    filtered_data = data[data["country"] == "Ethiopia"]
else:
    filtered_data = data[data["country"].isin(selected_countries)]
