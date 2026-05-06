import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Climate Data Analysis",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Ethiopia Climate Data Analysis")
st.caption("Women in Tech Program · Paper Airplanes")
st.divider()

# ── Load your existing dataset ─────────────────────────────
@st.cache_data
def load_data():
    return pd.read_csv("notebooks/data/YOUR_FILE_NAME.csv")  # ← change this

try:
    df = load_data()
    st.success(f"✅ Dataset loaded: {df.shape[0]:,} rows × {df.shape[1]} columns")

    # KPI row
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", f"{df.shape[0]:,}")
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    st.divider()

    # Tabs
    tab1, tab2, tab3 = st.tabs(["📋 Data", "📈 Charts", "📊 Statistics"])

    with tab1:
        st.dataframe(df.head(100), use_container_width=True)

    with tab2:
        num_cols = df.select_dtypes(include="number").columns.tolist()
        if num_cols:
            x = st.selectbox("X axis", df.columns.tolist())
            y = st.selectbox("Y axis", num_cols)
            chart = st.selectbox("Chart type", ["Bar", "Line", "Scatter"])
            if chart == "Bar":
                fig = px.bar(df, x=x, y=y)
            elif chart == "Line":
                fig = px.line(df, x=x, y=y)
            else:
                fig = px.scatter(df, x=x, y=y)
            st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.dataframe(df.describe().round(2), use_container_width=True)

except Exception as e:
    st.error(f"❌ Error loading data: {e}")
