from pathlib import Path
import pandas as pd


class DataLoader:

    @staticmethod
    def load_data():

        # ROOT DIRECTORY
        ROOT_DIR = Path(__file__).resolve().parent.parent

        # DATA FOLDER
        data_folder = ROOT_DIR / "data"

        # CHECK FOLDER EXISTS
        if not data_folder.exists():

            raise FileNotFoundError(
                f"Data folder not found: {data_folder}"
            )

        # FIND ALL CSV FILES
        csv_files = list(data_folder.glob("*.csv"))

        # CHECK CSV FILES
        if len(csv_files) == 0:

            raise FileNotFoundError(
                f"No CSV files found in: {data_folder}"
            )

        # STORE DATAFRAMES
        dataframes = []

        # LOAD EACH FILE
        for file in csv_files:

            df = pd.read_csv(file)

            # CLEAN COLUMN NAMES
            df.columns = (
                df.columns
                .str.strip()
                .str.lower()
            )

            # ADD COUNTRY COLUMN
            df["country"] = file.stem.lower()

            dataframes.append(df)

        # COMBINE ALL DATA
        combined_data = pd.concat(
            dataframes,
            ignore_index=True
        )

        return combined_data
