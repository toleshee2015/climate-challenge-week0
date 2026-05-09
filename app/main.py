
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st

from src.data_loader import DataLoader
from src.analysis import ClimateAnalysis
from src.visualizer import Visualizer
from src.utils import Utils


class ClimateDashboard:

    def __init__(self):

        self.data = DataLoader.load_data()

        self.country_flags = Utils.get_country_flags()
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
    # SIDEBAR
    # -----------------------------------
    def create_comparison_table(data, selected_column):

    # Normalize column names
    data.columns = data.columns.str.strip().str.lower()

    # Normalize selected column too
    selected_column = selected_column.lower()

    # Check columns
    required_columns = ["country", "year", selected_column]

    for col in required_columns:
        if col not in data.columns:
            raise ValueError(f"Column '{col}' not found")

    # Create pivot table
    comparison = data.pivot_table(
        index="year",
        columns="country",
        values=selected_column
    )

    return comparison
    # DASHBOARD
    # -----------------------------------
    def dashboard(self):

        st.title("🌍 Africa Climate Dashboard")

        st.subheader("📊 Quick Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", self.filtered_data.shape[0])

        col2.metric("Columns", self.filtered_data.shape[1])

        col3.metric(
            "Average",
            ClimateAnalysis.calculate_average(
                self.filtered_data,
                self.selected_column
            )
        )

        # dataset preview
        st.subheader("📁 Dataset Preview")

        st.dataframe(self.filtered_data.head(10))

        # comparison
        st.subheader("🌍 Country Comparison")

        comparison = ClimateAnalysis.create_comparison_table(
            self.filtered_data,
            self.selected_column
        )

        Visualizer.show_chart(
            "Line Chart",
            comparison
        )

        # single chart
        st.subheader(f"📈 {self.chart_type}")

        Visualizer.show_chart(
            self.chart_type,
            self.filtered_data[[self.selected_column]]
        )

        # ranking
        st.subheader("🔥 Top Warming Countries")

        ranking = ClimateAnalysis.generate_ranking(
            self.filtered_data,
            self.selected_column
        )

        st.dataframe(ranking)

        st.bar_chart(
            ranking.set_index("Country")
        )

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
