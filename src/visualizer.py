import streamlit as st


class Visualizer:

    @staticmethod
    def show_chart(chart_type, data, column=None):

        if chart_type == "Line Chart":

            st.line_chart(data)

        elif chart_type == "Bar Chart":

            if column:
                st.bar_chart(data.set_index("year")[column])
            else:
                st.bar_chart(data)

        elif chart_type == "Area Chart":

            if column:
                st.area_chart(data.set_index("year")[column])
            else:
                st.area_chart(data)
