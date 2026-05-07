import pandas as pd
import plotly.express as px

def get_temperature_stats(df):
    """Return basic temperature statistics"""
    stats = {
        "avg_temp": round(df["T2M"].mean(), 2),
        "max_temp": round(df["T2M_MAX"].max(), 2),
        "min_temp": round(df["T2M_MIN"].min(), 2),
        "temp_range": round(df["T2M_RANGE"].mean(), 2)
    }
    return stats

def plot_temperature_trend(df):
    """Plot temperature over time"""
    fig = px.line(
        df, x="DOY", y="T2M",
        title="Daily Temperature Trend",
        labels={"DOY": "Day of Year", "T2M": "Temperature (°C)"}
    )
    return fig

def plot_humidity_chart(df):
    """Plot humidity distribution"""
    fig = px.histogram(
        df, x="RH2M",
        title="Humidity Distribution",
        labels={"RH2M": "Relative Humidity (%)"}
    )
    return fig

def plot_wind_speed(df):
    """Plot wind speed over time"""
    fig = px.line(
        df, x="DOY", y="WS2M",
        title="Wind Speed Trend",
        labels={"DOY": "Day of Year", "WS2M": "Wind Speed (m/s)"}
    )
    return fig

def get_yearly_summary(df):
    """Return yearly averages"""
    return df.groupby("YEAR")[["T2M", "RH2M", "WS2M", "PRECTOTCORR"]].mean().reset_index()
