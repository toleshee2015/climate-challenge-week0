import streamlit as st


class Visualizer:

    @staticmethod
    def show_chart(chart_type, data):

        if chart_type == "Line Chart":
            st.line_chart(data)

        elif chart_type == "Bar Chart":
            st.bar_chart(data)

        elif chart_type == "Area Chart":
            st.area_chart(data)
