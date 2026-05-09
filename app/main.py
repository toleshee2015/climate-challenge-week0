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

        # Load data
        self.data = DataLoader.load_data()

        # FIX: normalize column names (this fixes KeyError: 'country')
        self.data.columns = (
            self.data.columns
            .str.strip()
            .str.lower()
        )

        # Debug (remove later if you want)
        # st.write(self.data.columns)

        self.country_flags = Utils.get_country_flags()

        # default values (avoid attribute errors)
        self.filtered_data = self.data.copy()
        self.selected_column = None
        self.chart_type = None

    # -----------------------------------
    # PAGE SETUP
    # -----------------------------------
    def setup_page(self):

        st.set_page_config(
            page_title="Africa Climate Dashboard",
            page_icon="🌍",
            layout="wide"
        )

    # -----------------------------------
    # SIDEBAR CONTROLS
    # -----------------------------------
    def sidebar(self):

        st.sidebar.title("⚙ Settings")

        # Ensure 'country' exists before using it
        if "country" not in self.data.columns:
            st.error(f"'country' column not found. Available columns: {list(self.data.columns)}")
            st.stop()

        countries = sorted(self.data["country"].dropna().unique())

        selected_countries = st.sidebar.multiselect(
            "Select Countries",
            countries,
            default=countries[:3] if len(countries) >= 3 else countries
        )

        # numeric columns only
        numeric_columns = self.data.select_dtypes(include="number").columns.tolist()

        if not numeric_columns:
            st.error("No numeric columns found in dataset.")
            st.stop()

        self.selected_column = st.sidebar.selectbox(
            "Select Indicator",
            numeric_columns
        )

        self.chart_type = st.sidebar.selectbox(
            "Chart Type",
            ["Line Chart", "Bar Chart", "Area Chart"]
        )

        self.show_ranking = st.sidebar.checkbox("Show Ranking", True)

        self.show_notebook = st.sidebar.checkbox("Show Notebook Viewer", False)

        # FILTER DATA (safe utility function)
        self.filtered_data = Utils.filter_countries(
            self.data,
            selected_countries
        )

    # -----------------------------------
    # DASHBOARD
    # -----------------------------------
    def dashboard(self):

        st.title("🌍 Africa Climate Dashboard")

        # -------------------------
        # QUICK METRICS
        # -------------------------
        st.subheader("📊 Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", self.filtered_data.shape[0])
        col2.metric("Columns", self.filtered_data.shape[1])

        avg = ClimateAnalysis.calculate_average(
            self.filtered_data,
            self.selected_column
        )

        col3.metric("Average", round(avg, 2))

        # -------------------------
        # DATA PREVIEW
        # -------------------------
        st.subheader("📁 Data Preview")
        st.dataframe(self.filtered_data.head(10), use_container_width=True)

        # -------------------------
        # COUNTRY COMPARISON
        # -------------------------
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

        # -------------------------
        # CHART VIEW
        # -------------------------
        st.subheader(f"📈 {self.chart_type}")

        Visualizer.show_chart(
            self.chart_type,
            self.filtered_data,
            self.selected_column
        )

        # -------------------------
        # RANKING
        # -------------------------
        if self.show_ranking:

            st.subheader("🔥 Country Ranking")

            ranking = ClimateAnalysis.generate_ranking(
                self.filtered_data,
                self.selected_column
            )

            st.dataframe(ranking, use_container_width=True)

            st.bar_chart(ranking.set_index("country"))

        # -------------------------
        # NOTEBOOK VIEWER
        # -------------------------
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
