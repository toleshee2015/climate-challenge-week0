import pandas as pd
import os

def load_data():
    """Load the Ethiopia climate dataset"""
    data_path = os.path.join(os.path.dirname(__file__), "C:\Data\ethiopia.csv")
    df = pd.read_csv(data_path)
    return df

def clean_data(df):
    """Clean and prepare the dataframe"""
    df = df.drop_duplicates()
    df = df.fillna(df.mean(numeric_only=True))
    return df
