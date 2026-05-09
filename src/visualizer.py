import streamlit as st


class Visualizer:

    @staticmethod
    def show_chart(chart_type, data, column=None):

        # -----------------------------
        # LINE CHART
        # -----------------------------
        if chart_type == "Line Chart":

            if column and column in data.columns:
                st.line_chart(data[column])
            else:
                st.line_chart(data)

        # -----------------------------
        # BAR CHART
        # -----------------------------
        elif chart_type == "Bar Chart":

            if column and column in data.columns:
                st.bar_chart(data[column])
            else:
                st.bar_chart(data)

        # -----------------------------
        # AREA CHART
        # -----------------------------
        elif chart_type == "Area Chart":

            if column and column in data.columns:
                st.area_chart(data[column])
            else:
                st.area_chart(data)

        # -----------------------------
        # FALLBACK
        # -----------------------------
        else:
            st.warning("Invalid chart type selected")
