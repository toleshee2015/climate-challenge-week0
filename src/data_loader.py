import pandas as pd
from pathlib import Path


class DataLoader:

    @staticmethod
    def load_data():

        BASE_DIR = Path(__file__).resolve().parent.parent

        file_path = BASE_DIR / "data" / "ethiopia.csv"

        return pd.read_csv(file_path)
