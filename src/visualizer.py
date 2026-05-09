import plotly.express as px


class Visualizer:

    @staticmethod
    def show_chart(chart_type, df, column):

        if chart_type == "Line Chart":

            fig = px.line(
                df,
                x="doy" if "doy" in df.columns else df.index,
                y=column,
                title=f"{column} Trend"
            )

        elif chart_type == "Bar Chart":

            yearly = (
                df.groupby("year", as_index=False)[column]
                .mean()
            )

            fig = px.bar(
                yearly,
                x="year",
                y=column,
                title=f"Yearly Average {column}"
            )

        elif chart_type == "Histogram":

            fig = px.histogram(
                df,
                x=column,
                title=f"Distribution of {column}"
            )

        else:

            fig = px.line(df, y=column)

        return fig
