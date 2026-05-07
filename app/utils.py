import pandas as pd
from pathlib import Path

def load_data():
    """Load the Ethiopia climate dataset"""

    BASE_DIR = Path(__file__).resolve().parent.parent
    data_path = BASE_DIR / "data" / "ethiopia.csv"

    df = pd.read_csv(data_path)

    return df


def clean_data(df):
    """Clean and prepare the dataframe"""

    df = df.drop_duplicates()
    df = df.fillna(df.mean(numeric_only=True))

    return df
