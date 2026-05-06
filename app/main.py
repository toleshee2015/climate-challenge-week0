import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ── Page config ──────────────────────────────────────────
st.set_page_config(page_title="Ethiopia Climate Dashboard", layout="wide")
st.title("🌍 Ethiopia Climate Dashboard")

# ── Load data ────────────────────────────────────────────
@st.cache_data
def load_data():
    return pd.read_csv("data/ethiopia.csv")

df = load_data()

# ── Sidebar filters ──────────────────────────────────────
st.sidebar.header("🔧 Filters")

# Column selector
all_columns = df.columns.tolist()
numeric_columns = df.select_dtypes(include="number").columns.tolist()

selected_column = st.sidebar.selectbox("Select a column to visualize", numeric_columns)

# Row slider
row_count = st.sidebar.slider("Number of rows to display", 5, len(df), 50)

# ── Section 1: Raw Data Preview ──────────────────────────
st.subheader("📋 Data Preview")
st.dataframe(df.head(row_count), use_container_width=True)

# ── Section 2: Summary Statistics ────────────────────────
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# ── Section 3: Line Chart ─────────────────────────────────
st.subheader(f"📈 Line Chart — {selected_column}")
st.line_chart(df[selected_column])

# ── Section 4: Bar Chart ──────────────────────────────────
st.subheader(f"📊 Bar Chart — {selected_column}")
st.bar_chart(df[selected_column].head(50))

# ── Section 5: Histogram ──────────────────────────────────
st.subheader(f"🔢 Distribution — {selected_column}")
fig, ax = plt.subplots()
ax.hist(df[selected_column].dropna(), bins=30, color="steelblue", edgecolor="white")
ax.set_xlabel(selected_column)
ax.set_ylabel("Frequency")
st.pyplot(fig)

# ── Section 6: Correlation Heatmap ───────────────────────
if len(numeric_columns) > 1:
    st.subheader("🔥 Correlation Heatmap")
    import numpy as np
    corr = df[numeric_columns].corr()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    im = ax2.imshow(corr, cmap="coolwarm")
    ax2.set_xticks(range(len(numeric_columns)))
    ax2.set_yticks(range(len(numeric_columns)))
    ax2.set_xticklabels(numeric_columns, rotation=45, ha="right")
    ax2.set_yticklabels(numeric_columns)
    plt.colorbar(im, ax=ax2)
    st.pyplot(fig2)

# ── Section 7: Compare Two Columns ───────────────────────
if len(numeric_columns) >= 2:
    st.subheader("⚖️ Compare Two Columns")
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("X axis", numeric_columns, index=0)
    with col2:
        y_axis = st.selectbox("Y axis", numeric_columns, index=1)

    fig3, ax3 = plt.subplots()
    ax3.scatter(df[x_axis], df[y_axis], alpha=0.5, color="coral")
    ax3.set_xlabel(x_axis)
    ax3.set_ylabel(y_axis)
    st.pyplot(fig3)

st.success("✅ Dashboard loaded successfully!")
