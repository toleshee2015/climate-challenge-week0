import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
from utils import load_data, clean_data
from analysis import (
    get_temperature_stats,
    plot_line_chart,
    plot_bar_chart,
    plot_histogram,
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

# Load and clean data
@st.cache_data
def get_data():
    df = load_data()
    df = clean_data(df)
    return df

df = get_data()

# Title
st.title("🌍 Ethiopia Climate Dashboard")
st.markdown("Interactive dashboard for exploring Ethiopia climate data.")

st.divider()

# Sidebar
st.sidebar.header("⚙️ Settings")

# Climate variable selector
climate_vars = ["T2M", "T2M_MAX", "T2M_MIN", "T2M_RANGE",
                "RH2M", "WS2M", "WS2M_MAX", "PRECTOTCORR"]
selected_var = st.sidebar.selectbox("Select Climate Variable", climate_vars)

# Chart type selector
chart_type = st.sidebar.selectbox(
    "Chart Type",
    ["Line Chart", "Bar Chart", "Histogram"]
)

# Notebook viewer toggle
show_notebook = st.sidebar.checkbox("Show Notebook Viewer")

# Year filter
available_years = sorted(df["YEAR"].unique().tolist())
selected_years = st.sidebar.multiselect(
    "Select Years",
    available_years,
    default=available_years
)

# Filter data by selected years
if selected_years:
    filtered_df = df[df["YEAR"].isin(selected_years)]
else:
    filtered_df = df

st.divider()

# KPI Metrics
st.subheader("📊 Key Climate Metrics")
stats = get_temperature_stats(filtered_df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("🌡️ Avg Temperature", f"{stats['avg_temp']} °C")
col2.metric("🔺 Max Temperature", f"{stats['max_temp']} °C")
col3.metric("🔻 Min Temperature", f"{stats['min_temp']} °C")
col4.metric("📏 Avg Temp Range", f"{stats['temp_range']} °C")

st.divider()

# Main Chart
st.subheader(f"📈 {chart_type} — {selected_var}")

fig = None

if chart_type == "Line Chart":
    fig = plot_line_chart(filtered_df, selected_var)
elif chart_type == "Bar Chart":
    fig = plot_bar_chart(filtered_df, selected_var)
elif chart_type == "Histogram":
    fig = plot_histogram(filtered_df, selected_var)

if fig is not None:
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning(f"Could not generate chart for '{selected_var}'")

st.divider()

# Temperature and Humidity side by side
st.subheader("🌡️ Temperature & 💧 Humidity Overview")

col1, col2 = st.columns(2)

with col1:
    temp_fig = plot_temperature_trend(filtered_df)
    if temp_fig is not None:
        st.plotly_chart(temp_fig, use_container_width=True)
    else:
        st.warning("Temperature chart unavailable")

with col2:
    humidity_fig = plot_humidity_chart(filtered_df)
    if humidity_fig is not None:
        st.plotly_chart(humidity_fig, use_container_width=True)
    else:
        st.warning("Humidity chart unavailable")

st.divider()

# Wind Speed
st.subheader("💨 Wind Speed Trend")
wind_fig = plot_wind_speed(filtered_df)
if wind_fig is not None:
    st.plotly_chart(wind_fig, use_container_width=True)
else:
    st.warning("Wind speed chart unavailable")

st.divider()

# Yearly Summary Table
st.subheader("📅 Yearly Summary")
yearly_df = get_yearly_summary(filtered_df)
st.dataframe(yearly_df, use_container_width=True)

st.divider()

# Notebook Viewer
if show_notebook:
    st.subheader("📓 Notebook Viewer")
    notebook_path = os.path.join(
        os.path.dirname(__file__),
        "../notebooks/ethiopia_eda.ipynb"
    )
    if os.path.exists(notebook_path):
        import nbformat
        from nbconvert import HTMLExporter
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
        exporter = HTMLExporter()
        body, _ = exporter.from_notebook_node(nb)
        st.components.v1.html(body, height=800, scrolling=True)
    else:
        st.warning("Notebook file not found.")

st.divider()

# Raw Data
with st.expander("🔍 View Raw Data"):
    st.dataframe(filtered_df, use_container_width=True)
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="⬇️ Download Data as CSV",
        data=csv,
        file_name="ethiopia_climate_data.csv",
        mime="text/csv"
    )
