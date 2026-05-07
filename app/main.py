import streamlit as st
from utils import load_data, clean_data
from analysis import (
    get_temperature_stats,
    plot_temperature_trend,
    plot_humidity_chart,
    plot_wind_speed,
    get_yearly_summary
)

# Page config
st.set_page_config(
    page_title="Ethiopia Climate Dashboard",
    page_icon="🌍",
    layout="wide"
)

# Load data
df = load_data()
df = clean_data(df)

# Title
st.title("🌍 Ethiopia Climate Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
years = sorted(df["YEAR"].unique())
selected_year = st.sidebar.selectbox("Select Year", ["All"] + list(years))

if selected_year != "All":
    df = df[df["YEAR"] == selected_year]

# KPI Metrics row
st.subheader("📊 Key Climate Metrics")
stats = get_temperature_stats(df)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Temperature", f"{stats['avg_temp']} °C")
col2.metric("Max Temperature", f"{stats['max_temp']} °C")
col3.metric("Min Temperature", f"{stats['min_temp']} °C")
col4.metric("Avg Temp Range", f"{stats['temp_range']} °C")

st.divider()

# Charts row
st.subheader("📈 Temperature Trend")
st.plotly_chart(plot_temperature_trend(df), use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("💧 Humidity Distribution")
    st.plotly_chart(plot_humidity_chart(df), use_container_width=True)

with col2:
    st.subheader("💨 Wind Speed Trend")
    st.plotly_chart(plot_wind_speed(df), use_container_width=True)

# Yearly summary table
st.subheader("📅 Yearly Summary")
st.dataframe(get_yearly_summary(df), use_container_width=True)

# Data preview
with st.expander("🔍 View Raw Data"):
    st.dataframe(df, use_container_width=True)
