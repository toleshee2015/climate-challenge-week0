import pandas as pd
import plotly.express as px


class ClimateAnalysis:

    @staticmethod
    def calculate_average(df, column):
        if column not in df.columns:
            return 0
        return df[column].mean()

    @staticmethod
    def get_temperature_stats(df):
        return {
            "avg_temp": df["t2m"].mean() if "t2m" in df.columns else None,
            "max_temp": df["t2m_max"].max() if "t2m_max" in df.columns else None,
            "min_temp": df["t2m_min"].min() if "t2m_min" in df.columns else None,
            "temp_range": df["t2m_range"].mean() if "t2m_range" in df.columns else None
        }

    @staticmethod
    def create_comparison_table(df, selected_column):
        if "year" not in df.columns:
            return df

        return df.pivot_table(
            index="year",
            values=selected_column,
            aggfunc="mean"
        )

    @staticmethod
    def generate_ranking(df, column):
        if "year" not in df.columns:
            return df

        return (
            df.groupby("year")[column]
            .mean()
            .reset_index()
            .sort_values(column, ascending=False)
        )

    @staticmethod
    def plot_line_chart(df, column):
        if column not in df.columns:
            return None

        if "doy" in df.columns:
            df = df.sort_values("doy")

        return px.line(df, x="doy", y=column, title=f"{column} Over Time")

    @staticmethod
    def plot_bar_chart(df, column):
        if column not in df.columns:
            return None

        if "year" not in df.columns:
            return None

        yearly = df.groupby("year")[column].mean().reset_index()

        return px.bar(yearly, x="year", y=column, title=f"Yearly Average of {column}")

    @staticmethod
    def plot_histogram(df, column):
        if column not in df.columns:
            return None

        return px.histogram(df, x=column)
