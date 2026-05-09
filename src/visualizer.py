import streamlit as st


class Visualizer:

    @staticmethod
    def show_chart(chart_type, data, column=None):

        # Safety check
        if data is None or len(data) == 0:
            st.warning("No data available")
            return

        # LINE CHART
        if chart_type == "Line Chart":

            if column and column in data.columns:
                st.line_chart(data.set_index(data.columns[0])[column])
            else:
                st.line_chart(data)

        # BAR CHART
        elif chart_type == "Bar Chart":

            if column and column in data.columns:
                st.bar_chart(data[column])
            else:
                st.bar_chart(data)

        # AREA CHART
        elif chart_type == "Area Chart":

            if column and column in data.columns:
                st.area_chart(data[column])
            else:
                st.area_chart(data)

        else:
            st.warning("Invalid chart type selected")
