import pandas as pd


class ClimateAnalysis:

    @staticmethod
    def calculate_average(df, column):

        if column not in df.columns:
            return 0

        return df[column].mean()

    @staticmethod
    def create_trend_data(df, column):

        if "year" not in df.columns:
            return pd.DataFrame()

        return (
            df.groupby("year", as_index=False)[column]
            .mean()
        )

    @staticmethod
    def generate_ranking(df, column):

        return (
            df.groupby("year")[column]
            .mean()
            .reset_index()
            .sort_values(column, ascending=False)
        )
