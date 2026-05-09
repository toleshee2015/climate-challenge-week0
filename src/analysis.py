import pandas as pd
import plotly.express as px

def get_temperature_stats(df):
    stats = {
        "avg_temp": round(df["T2M"].mean(), 2),
        "max_temp": round(df["T2M_MAX"].max(), 2),
        "min_temp": round(df["T2M_MIN"].min(), 2),
        "temp_range": round(df["T2M_RANGE"].mean(), 2)
    }
    return stats

def plot_line_chart(df, column):
    """Generic line chart for any climate variable"""
    if column not in df.columns:
        return None
    df = df.copy()
    df = df.sort_values("DOY")
    fig = px.line(
        df,
        x="DOY",
        y=column,
        color="YEAR" if "YEAR" in df.columns else None,
        title=f"{column} Over Time",
        labels={"DOY": "Day of Year", column: column}
    )
    return fig

def plot_bar_chart(df, column):
    """Generic bar chart for any climate variable"""
    if column not in df.columns:
        return None
    df = df.copy()
    yearly = df.groupby("YEAR")[column].mean().reset_index()
    fig = px.bar(
        yearly,
        x="YEAR",
        y=column,
        title=f"Yearly Average of {column}",
        labels={"YEAR": "Year", column: column}
    )
    return fig

def plot_histogram(df, column):
    """Generic histogram for any climate variable"""
    if column not in df.columns:
        return None
    fig = px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}",
        labels={column: column}
    )
    return fig

def plot_temperature_trend(df):
    return plot_line_chart(df, "T2M")

def plot_humidity_chart(df):
    return plot_histogram(df, "RH2M")

def plot_wind_speed(df):
    return plot_line_chart(df, "WS2M")

def get_yearly_summary(df):
    return df.groupby("YEAR")[
        ["T2M", "RH2M", "WS2M", "PRECTOTCORR"]
    ].mean().reset_index()
