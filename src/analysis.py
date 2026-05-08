class ClimateAnalysis:

    @staticmethod
    def get_numeric_columns(data):

        return data.select_dtypes(include=["number"]).columns.tolist()

    @staticmethod
    def calculate_average(data, column):

        return round(data[column].mean(), 2)

    @staticmethod
    def generate_ranking(data, selected_column):

        ranking = (
            data
            .groupby("country")[selected_column]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        ranking.columns = ["Country", f"Avg {selected_column}"]

        return ranking

    @staticmethod
    def create_comparison_table(data, selected_column):

        return data.pivot_table(
            index="year" if "year" in data.columns else data.index,
            columns="country",
            values=selected_column
        )
