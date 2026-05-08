class ClimateStatistics:
    def __init__(self, dataframe):
        self.df = dataframe

    def average_temperature(self):
        return round(self.df["temperature"].mean(), 2)

    def max_temperature(self):
        return round(self.df["temperature"].max(), 2)

    def min_temperature(self):
        return round(self.df["temperature"].min(), 2)

    def temperature_range(self):
        return round(
            self.df["temperature"].max() - self.df["temperature"].min(),
            2,
        )
