import pandas as pd
import plotly.express as px


class ClimateAnalysis:

    # -----------------------------
    # BASIC STATS
    # -----------------------------
    @staticmethod
    def calculate_average(df, column):
        if column not in df.columns:
            return 0
        return df[column].mean()

    # -----------------------------
    # TEMPERATURE STATS
    # -----------------------------
    @staticmethod
    def get_temperature_stats(df):
        return {
            "avg_temp": df["t2m"].mean(),
            "max_temp": df["t2m_max"].max(),
            "min_temp": df["t2m_min"].min(),
            "temp_range": df["t2m_range"].mean()
        }

    # -----------------------------
    # COMPARISON TABLE
    # -----------------------------
    @staticmethod
    def create_comparison_table(df, selected_column):
        if "year" not in df.columns:
            return df

        return df.pivot_table(
            index="year",
            values=selected_column,
            aggfunc="mean"
        )

    # -----------------------------
    # RANKING
    # -----------------------------
    @staticmethod
    def generate_ranking(df, column):
        return (
            df.groupby("year")[column]
            .mean()
            .reset_index()
            .sort_values(column, ascending=False)
        )

    # -----------------------------
    # PLOTLY LINE CHART
    # -----------------------------
    @staticmethod
    def plot_line_chart(df, column):
        if column not in df.columns:
            return None

        df = df.sort_values("doy")

        return px.line(
            df,
            x="doy",
            y=column,
            title=f"{column} Over Time"
        )

    # -----------------------------
    # PLOTLY BAR CHART
    # -----------------------------
    @staticmethod
    def plot_bar_chart(df, column):
        if column not in df.columns:
            return None

        yearly = df.groupby("year")[column].mean().reset_index()

        return px.bar(
            yearly,
            x="year",
            y=column,
            title=f"Yearly Average of {column}"
        )

    # -----------------------------
    # HISTOGRAM
    # -----------------------------
    @staticmethod
    def plot_histogram(df, column):
        return px.histogram(df, x=column)
