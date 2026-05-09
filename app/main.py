import sys
from pathlib import Path

import streamlit as st

# -----------------------------------
# ROOT SETUP
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

        # Load dataset
        self.data = DataLoader.load_data()

        # Clean columns
        self.data.columns = (
            self.data.columns
            .str.strip()
            .str.lower()
        )

        # Country flags
        self.country_flags = Utils.get_country_flags()

    # -----------------------------------
    # PAGE CONFIG
    # -----------------------------------
    def setup_page(self):

        st.set_page_config(
            page_title="Africa Climate Dashboard",
            page_icon="🌍",
            layout="wide"
        )

    # -----------------------------------
    # SIDEBAR
    # -----------------------------------
    def sidebar(self):

        st.sidebar.title("⚙ Dashboard Settings")

        # Country filter
        countries = sorted(
            self.data["country"].unique()
        )

        selected_countries = st.sidebar.multiselect(
            "Select Countries",
            countries,
            default=countries[:3]
        )

        # Column selection
        numeric_columns = (
            self.data
            .select_dtypes(include="number")
            .columns
            .tolist()
        )

        self.selected_column = st.sidebar.selectbox(
            "Select Climate Indicator",
            numeric_columns
        )

        # Chart selection
        self.chart_type = st.sidebar.selectbox(
            "Select Chart Type",
            [
                "Line Chart",
                "Bar Chart",
                "Area Chart"
            ]
        )

        # Optional tools
        st.sidebar.subheader("🧰 Advanced Tools")

        self.show_ranking = st.sidebar.checkbox(
            "Show Country Ranking",
            value=True
        )

        self.show_notebook = st.sidebar.checkbox(
            "Show Notebook Viewer",
            value=False
        )

        # Filter data
        self.filtered_data = Utils.filter_countries(
            self.data,
            selected_countries
        )

    # -----------------------------------
    # DASHBOARD
    # -----------------------------------
    def dashboard(self):

        st.title("🌍 Africa Climate Dashboard")

        # -----------------------------------
        # OVERVIEW
        # -----------------------------------
        st.subheader("📊 Quick Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Rows",
            self.filtered_data.shape[0]
        )

        col2.metric(
            "Columns",
            self.filtered_data.shape[1]
        )

        average_value = ClimateAnalysis.calculate_average(
            self.filtered_data,
            self.selected_column
        )

        col3.metric(
            "Average",
            round(average_value, 2)
        )

        # -----------------------------------
        # DATA PREVIEW
        # -----------------------------------
        st.subheader("📁 Dataset Preview")

        st.dataframe(
            self.filtered_data.head(10),
            use_container_width=True
        )

        # -----------------------------------
        # COMPARISON TABLE
        # -----------------------------------
        st.subheader("🌍 Country Comparison")

        comparison = ClimateAnalysis.create_comparison_table(
            self.filtered_data,
            self.selected_column
        )

        st.dataframe(comparison)

        Visualizer.show_chart(
            "Line Chart",
            comparison
        )

        # -----------------------------------
        # VISUALIZATION
        # -----------------------------------
        st.subheader(f"📈 {self.chart_type}")

        Visualizer.show_chart(
            self.chart_type,
            self.filtered_data,
            self.selected_column
        )

        # -----------------------------------
        # RANKING
        # -----------------------------------
        if self.show_ranking:

            st.subheader("🔥 Top Warming Countries")

            ranking = ClimateAnalysis.generate_ranking(
                self.filtered_data,
                self.selected_column
            )

            st.dataframe(
                ranking,
                use_container_width=True
            )

            st.bar_chart(
                ranking.set_index("country")
            )

        # -----------------------------------
        # NOTEBOOK VIEWER
        # -----------------------------------
        if self.show_notebook:

            st.subheader("📓 Notebook Integration")

            NotebookViewer.display_notebook_info()

    # -----------------------------------
    # RUN
    # -----------------------------------
    def run(self):

        self.setup_page()

        self.sidebar()

        self.dashboard()


if __name__ == "__main__":

    app = ClimateDashboard()

    app.run()
