import plotly.express as px


class ClimateVisualizer:
    def __init__(self, dataframe):
        self.df = dataframe

    def line_chart(self, x_column, y_column, title):
        fig = px.line(
            self.df,
            x=x_column,
            y=y_column,
            title=title,
        )
        return fig

    def bar_chart(self, x_column, y_column, title):
        fig = px.bar(
            self.df,
            x=x_column,
            y=y_column,
            title=title,
        )
        return fig

    def scatter_chart(self, x_column, y_column, title):
        fig = px.scatter(
            self.df,
            x=x_column,
            y=y_column,
            title=title,
        )
        return fig
