import pandas as pd
from pathlib import Path

def load_data():

    BASE_DIR = Path(__file__).resolve().parent.parent
    data_path = BASE_DIR / "data" / "ethiopia.csv"

    print("BASE_DIR:", BASE_DIR)
    print("DATA PATH:", data_path)
    print("FILE EXISTS:", data_path.exists())

    df = pd.read_csv(data_path)

    return df

def clean_data(df):
    """Clean and prepare the dataframe"""

    df = df.drop_duplicates()
    df = df.fillna(df.mean(numeric_only=True))

    return df
