
import streamlit as st

from src.data_loader import DataLoader
from src.analysis import ClimateAnalysis
from src.visualizer import Visualizer
from src.utils import Utils


class ClimateDashboard:

    def __init__(self):

        self.data = DataLoader.load_data()

        self.country_flags = Utils.get_country_flags()

    from src.data_loader import DataLoader
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
    def sidebar(self):

        st.sidebar.header("🌍 Country Comparison")

        country_col = Utils.find_country_column(self.data)

        if country_col:

            countries = sorted(self.data[country_col].unique())

            country_options = [
                f"{self.country_flags.get(c, '🌍')} {c}"
                for c in countries
            ]

            selected_display = st.sidebar.multiselect(
                "Select countries",
                options=country_options,
                default=country_options[:2]
            )

            selected_countries = [
                c.split(" ", 1)[1]
                for c in selected_display
            ]

            self.filtered_data = self.data[
                self.data[country_col].isin(selected_countries)
            ]

        else:
            self.filtered_data = self.data

        self.numeric_columns = ClimateAnalysis.get_numeric_columns(
            self.filtered_data
        )

        self.selected_column = st.sidebar.selectbox(
            "Select variable",
            self.numeric_columns
        )

        self.chart_type = st.sidebar.selectbox(
            "Chart Type",
            ["Line Chart", "Bar Chart", "Area Chart"]
        )

        # custom parameter
        self.window_size = st.sidebar.slider(
            "Custom Smoothing Parameter",
            1,
            10,
            3
        )

    # -----------------------------------
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
