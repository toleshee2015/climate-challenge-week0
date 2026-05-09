from pathlib import Path
import pandas as pd


class DataLoader:

    @staticmethod
    def load_data():

        data_path = Path("data/ethiopia.csv")

        return pd.read_csv(data_path)
