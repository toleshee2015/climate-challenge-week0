import pandas as pd


class ClimateAnalysis:

    @staticmethod
    def calculate_average(data, column):

        return data[column].mean()

    @staticmethod
    def create_comparison_table(data, selected_column):

        # Normalize columns
        data.columns = (
            data.columns
            .str.strip()
            .str.lower()
        )

        selected_column = selected_column.lower()

        required_columns = [
            "country",
            "year",
            selected_column
        ]

        for col in required_columns:

            if col not in data.columns:
                raise ValueError(
                    f"Column '{col}' not found"
                )

        comparison = data.pivot_table(
            index="year",
            columns="country",
            values=selected_column
        )

        return comparison

    @staticmethod
    def generate_ranking(data, column):

        ranking = (
            data.groupby("country")[column]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        return ranking
