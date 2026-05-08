class ClimateFilter:
    def __init__(self, dataframe):
        self.df = dataframe

    def filter_by_year(self, year_column, selected_year):
        if selected_year == "All":
            return self.df

        return self.df[self.df[year_column] == selected_year]

    def custom_filter(self, column_name, min_value, max_value):
        return self.df[
            (self.df[column_name] >= min_value)
            & (self.df[column_name] <= max_value)
        ]
