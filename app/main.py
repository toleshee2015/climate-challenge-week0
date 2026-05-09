import pandas as pd
import streamlit as st

from src.analysis import ClimateAnalysis
from src.visualizer import Visualizer


class App:

    def __init__(self):
        self.df = None
        self.filtered_data = None
        self.selected_column = None
        self.chart_type = None

    def load_data(self):
        # adjust file name if needed
        self.df = pd.read_csv("data/climate.csv")

        # ✅ IMPORTANT FIX: create missing column here
        if "date" in self.df.columns:
            self.df["date"] = pd.to_datetime(self.df["date"])
            self.df["year"] = self.df["date"].dt.year

        self.filtered_data = self.df

    def dashboard(self):

        st.title("🌍 Climate Dashboard")

        st.write("📊 Overview")
        st.write(self.filtered_data.shape)

        st.write("📁 Dataset Preview")
        st.dataframe(self.filtered_data.head())

        st.write("📈 Trend Over Time")

        if self.selected_column:
            Visualizer.show_chart(
                self.chart_type,
                self.filtered_data,
                self.selected_column
            )

    def run(self):
        self.load_data()
        self.dashboard()


if __name__ == "__main__":
    app = App()
    app.run()
