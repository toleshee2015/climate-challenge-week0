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

        # Clean columns
        self.data.columns = (
            self.data.columns
            .str.strip()
            .str.lower()
        )

        self.filtered_data = self.data.copy()
        self.selected_column = None
        self.chart_type = None
        self.show_notebook = False

    # -----------------------------------
    # PAGE CONFIGURATION
    # -----------------------------------
    def setup_page(self):

        st.set_page_config(
            page_title="Climate Analysis Interface",
            page_icon="🌍",
            layout="wide"
        )

    # -----------------------------------
    # SIDEBAR
    # -----------------------------------
    def sidebar(self):

        st.sidebar.title("⚙ CLIMATE VARIABLE")

        numeric_columns = self.data.select_dtypes(include="number").columns.tolist()

        self.selected_column = st.sidebar.selectbox(
            "Select Climate Variable",
            numeric_columns
        )

        self.chart_type = st.sidebar.selectbox(
            "Select Chart Type",
            ["Line Chart", "Bar Chart", "Histogram"]
        )

        self.show_notebook = st.sidebar.checkbox(
            "Show Notebook Integration",
            False
        )

        # Year Filter
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

    # -----------------------------------
    # DASHBOARD BODY
    # -----------------------------------
    def dashboard(self):

        st.title("🌍 Climate Change Dashboard")

        # -----------------------------
        # METRICS
        # -----------------------------
        st.subheader("📊 Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", self.filtered_data.shape[0])
        col2.metric("Columns", self.filtered_data.shape[1])

        avg_value = ClimateAnalysis.calculate_average(
            self.filtered_data,
            self.selected_column
        )

        col3.metric("Average", round(avg_value, 2))

        # -----------------------------
        # DATA PREVIEW
        # -----------------------------
        st.subheader("📁 Dataset Preview")

        st.dataframe(
            self.filtered_data.head(10),
            use_container_width=True
        )

        # -----------------------------
        # TREND ANALYSIS
        # -----------------------------
        st.subheader("📈 Trend Analysis")

        trend_data = ClimateAnalysis.create_trend_data(
            self.filtered_data,
            self.selected_column
        )

        st.line_chart(
            trend_data.set_index("year")
        )

        # -----------------------------
        # VISUALIZATION
        # -----------------------------
        st.subheader(f"📊 {self.chart_type}")

        fig = Visualizer.show_chart(
            self.chart_type,
            self.filtered_data,
            self.selected_column
        )

        st.plotly_chart(fig, use_container_width=True)

        # -----------------------------
        # RANKING
        # -----------------------------
        st.subheader("🔥 Ranking")

        ranking = ClimateAnalysis.generate_ranking(
            self.filtered_data,
            self.selected_column
        )

        st.dataframe(ranking)

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
