import sys
from pathlib import Path
import streamlit as st

# -----------------------------------
# ROOT PATH SETUP
# -----------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

# -----------------------------------
# IMPORT MODULES
# -----------------------------------
from src.data_loader import DataLoader
from src.analysis import ClimateAnalysis
from src.visualizer import Visualizer
from src.utils import Utils
from src.notebook_viewer import NotebookViewer


class ClimateDashboard:

    def __init__(self):

        self.data = DataLoader.load_data()

        # CLEAN COLUMN NAMES
        self.data.columns = (
            self.data.columns
            .str.strip()
            .str.lower()
        )

        self.filtered_data = self.data.copy()
        self.selected_column = None
        self.chart_type = None

    # -----------------------------------
    # PAGE SETUP
    # -----------------------------------
    def setup_page(self):

        st.set_page_config(
            page_title="Climate Dashboard",
            page_icon="🌍",
            layout="wide"
        )

    # -----------------------------------
    # SIDEBAR
    # -----------------------------------
    def sidebar(self):

        st.sidebar.title("⚙ Settings")

        numeric_columns = self.data.select_dtypes(include="number").columns.tolist()

        if not numeric_columns:
            st.error("No numeric columns found in dataset.")
            st.stop()

        self.selected_column = st.sidebar.selectbox(
            "Select Climate Variable",
            numeric_columns
        )

        self.chart_type = st.sidebar.selectbox(
            "Chart Type",
            ["Line Chart", "Bar Chart", "Area Chart"]
        )

        self.show_notebook = st.sidebar.checkbox(
            "Show Notebook Viewer",
            False
        )

        # Year filter (safe)
        if "year" in self.data.columns:

            years = sorted(self.data["year"].unique())

            selected_years = st.sidebar.multiselect(
                "Select Years",
                years,
                default=years[:3] if len(years) >= 3 else years
            )

            self.filtered_data = self.data[
                self.data["year"].isin(selected_years)
            ]

        else:

            self.filtered_data = self.data.copy()

    # -----------------------------------
    # DASHBOARD
    # -----------------------------------
    def dashboard(self):

        st.title("🌍 Climate Dashboard")

        # -----------------------------
        # OVERVIEW
        # -----------------------------
        st.subheader("📊 Overview")

        col1, col2 = st.columns(2)

        col1.metric("Rows", self.filtered_data.shape[0])
        col2.metric("Columns", self.filtered_data.shape[1])

        avg_value = ClimateAnalysis.calculate_average(
            self.filtered_data,
            self.selected_column
        )

        st.metric("Average Value", round(avg_value, 2))

        # -----------------------------
        # DATA PREVIEW
        # -----------------------------
        st.subheader("📁 Dataset Preview")

        st.dataframe(self.filtered_data.head(10))

        # -----------------------------
        # TREND OVER TIME
        # -----------------------------
        st.subheader("📈 Trend Over Time")

        if "year" in self.filtered_data.columns:

            trend_data = (
                self.filtered_data
                .groupby("year", as_index=False)[self.selected_column]
                .mean()
            )

            st.line_chart(trend_data.set_index("year"))

        else:

            st.line_chart(self.filtered_data[self.selected_column])

        # -----------------------------
        # VISUALIZER
        # -----------------------------
        st.subheader(f"📊 {self.chart_type}")

        Visualizer.show_chart(
            self.chart_type,
            self.filtered_data,
            self.selected_column
        )

        # -----------------------------
        # DISTRIBUTION
        # -----------------------------
        st.subheader("📊 Distribution")

        st.bar_chart(self.filtered_data[self.selected_column])

        # -----------------------------
        # NOTEBOOK VIEWER
        # -----------------------------
        if self.show_notebook:

            NotebookViewer.display_notebook_info()

    # -----------------------------------
    # RUN APP
    # -----------------------------------
    def run(self):

        self.setup_page()
        self.sidebar()
        self.dashboard()


# -----------------------------------
# ENTRY POINT
# -----------------------------------
if __name__ == "__main__":

    app = ClimateDashboard()
    app.run()
