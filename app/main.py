import streamlit as st
)

# Chart type selection
chart_type = st.sidebar.radio(
    "Select chart type",
    ["Line Chart", "Bar Chart", "Area Chart"]
)

# -----------------------------
# Display Dataset
# -----------------------------
st.subheader("Dataset Preview")
st.dataframe(data.head(num_rows))

# -----------------------------
# Dataset Information
# -----------------------------
st.subheader("Dataset Shape")
st.write(data.shape)

st.subheader("Column Names")
st.write(data.columns.tolist())

# -----------------------------
# Statistics
# -----------------------------
st.subheader("Statistics")
st.write(data.describe())

# -----------------------------
# Visualization Section
# -----------------------------
st.subheader(f"Visualization for {selected_column}")

chart_data = data[[selected_column]]

if chart_type == "Line Chart":
    st.line_chart(chart_data)

elif chart_type == "Bar Chart":
    st.bar_chart(chart_data)

elif chart_type == "Area Chart":
    st.area_chart(chart_data)

# -----------------------------
# Optional Filters
# -----------------------------
st.subheader("Filter Data")

min_value = float(data[selected_column].min())
max_value = float(data[selected_column].max())

range_values = st.slider(
    "Select value range",
    min_value,
    max_value,
    (min_value, max_value)
)

filtered_data = data[
    (data[selected_column] >= range_values[0]) &
    (data[selected_column] <= range_values[1])
]

st.write("Filtered Data")
st.dataframe(filtered_data)
