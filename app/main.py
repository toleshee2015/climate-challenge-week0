# =============================
# 1. IMPORTS
# =============================
import streamlit as st
import pandas as pd
from pathlib import Path


# =============================
# 2. DASHBOARD CLASS (OOP)
# =============================
class ClimateDashboard:

    def __init__(self):
        self.setup_page()
        self.load_data()
        self.country_flags = {
            "Ethiopia": "🇪🇹",
            "Kenya": "🇰🇪",
            "Nigeria": "🇳🇬",
            "Tanzania": "🇹🇿",
            "Sudan": "🇸🇩",
            "Uganda": "🇺🇬",
        }

    # -----------------------------
    # PAGE CONFIG
    # -----------------------------
    def setup_page(self):
        st.set_page_config(
            page_title="Africa Climate Analysis Dashboard",
            page_icon="🌍",
            layout="wide"
        )

        st.markdown("""
        <style>
        .main { background-color: #f5f7fa; }
        h1 { color: #1f77b4; }
        .stMetric {
            background-color: white;
            padding: 10px;
            border-radius: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    # -----------------------------
    # LOAD DATA
    # -----------------------------
    def load_data(self):
        BASE_DIR = Path(__file__).resolve().parent.parent
        file_path = BASE_DIR / "data" / "ethiopia.csv"
        self.data = pd.read_csv(file_path)

    # -----------------------------
    # SIDEBAR CONTROLS (WITH CUSTOM PARAMS)
    # -----------------------------
    def sidebar(self):

        st.sidebar.header("🌍5 African Country Comparison")

        country_col = None
        for col in self.data.columns:
            if col.lower() == "country":
                country_col = col
                break

        if country_col:

            countries = sorted(self.data[country_col].unique())

            country_options = [
                f"{self.country_flags.get(c, '🌍')} {c}" for c in countries
            ]

            selected_display = st.sidebar.multiselect(
                "Select countries",
                options=country_options,
                default=country_options[:2]
            )

            selected_countries = [
                c.split(" ", 1)[1] for c in selected_display
            ]

            self.filtered_data = self.data[self.data[country_col].isin(selected_countries)]

        else:
            self.filtered_data = self.data

        # -----------------------------
        # INDICATOR SELECTION
        # -----------------------------
        st.sidebar.header("📊 Indicator Selection")

        self.numeric_columns = self.filtered_data.select_dtypes(include=["number"]).columns.tolist()

        self.selected_column = st.sidebar.selectbox(
            "Select variable",
            self.numeric_columns
        )

        self.chart_type = st.sidebar.selectbox(
            "Chart type",
            ["Line Chart", "Bar Chart", "Area Chart"]
        )

        # -----------------------------
        # 🔥 CUSTOM USER PARAMETER (NEW FEATURE)
        # -----------------------------
        st.sidebar.header("⚙ Custom Analysis Parameters")

        self.smoothing_window = st.sidebar.slider(
            "Smoothing window (trend strength)",
            1,
            10,
            1
        )

    # -----------------------------
    # METRICS
    # -----------------------------
    def metrics(self):
        st.subheader("📊 Quick Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", self.filtered_data.shape[0])
        col2.metric("Columns", self.filtered_data.shape[1])
        col3.metric("Average", round(self.filtered_data[self.selected_column].mean(), 2))

    # -----------------------------
    # DATA PREVIEW
    # -----------------------------
    def preview(self):
        st.subheader("📁 Dataset Preview")

        display_data = self.filtered_data.copy()

        if "country" in display_data.columns:
            display_data["country"] = display_data["country"].apply(
                lambda x: f"{self.country_flags.get(x, '🌍')} {x}"
            )

        st.dataframe(display_data.head(10))

    # -----------------------------
    # COMPARISON CHART
    # -----------------------------
    def comparison(self):
        if "country" in self.filtered_data.columns:
            st.subheader(f"🌍 Country Comparison: {self.selected_column}")

            comparison = self.filtered_data.pivot_table(
                index="year" if "year" in self.filtered_data.columns else self.filtered_data.index,
                columns="country",
                values=self.selected_column
            )

            st.line_chart(comparison)

    # -----------------------------
    # SINGLE CHART
    # -----------------------------
    def chart(self):
        st.subheader(f"📈 {self.chart_type}: {self.selected_column}")

        chart_data = self.filtered_data[[self.selected_column]]

        if self.chart_type == "Line Chart":
            st.line_chart(chart_data)

        elif self.chart_type == "Bar Chart":
            st.bar_chart(chart_data)

        elif self.chart_type == "Area Chart":
            st.area_chart(chart_data)

    # -----------------------------
    # TOP WARMING COUNTRIES
    # -----------------------------
    def ranking(self):
        st.subheader("🌡️ Top Warming Countries Ranking")

        if all(col in self.filtered_data.columns for col in ["country", "year"]):

            warming_rank = (
                self.filtered_data
                .groupby("country")[self.selected_column]
                .mean()
                .sort_values(ascending=False)
                .reset_index()
            )

            warming_rank.columns = ["Country", f"Avg {self.selected_column}"]

            st.markdown("### 🔥 Highest Average Values")

            st.dataframe(warming_rank)

            st.markdown("### 📊 Visual Ranking")

            st.bar_chart(warming_rank.set_index("Country"))

            top_country = warming_rank.iloc[0]

            st.success(
                f"🔥 Highest average {self.selected_column}: "
                f"{top_country['Country']} ({top_country[f'Avg {self.selected_column}']:.2f})"
            )

    # -----------------------------
    # RUN APP
    # -----------------------------
    def run(self):

        st.title("🌍 Africa Climate Dashboard")

        st.markdown("""
        Interactive climate analysis across African countries with custom controls.
        """)

        self.sidebar()
        self.metrics()
        self.preview()
        self.comparison()
        self.chart()
        self.ranking()


# =============================
# RUN APPLICATION
# =============================
if __name__ == "__main__":
    app = ClimateDashboard()
    app.run()
