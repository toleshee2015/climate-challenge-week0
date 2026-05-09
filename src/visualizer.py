import streamlit as st


class Visualizer:

    @staticmethod
    def show_chart(chart_type, data, column):

        if data is None or data.empty:
            st.warning("No data available")
            return

        # safety check
        if column not in data.columns:
            st.error(f"Column '{column}' not found in dataset")
            return

        if chart_type == "line":

            # ✅ FIX: use correct index safely
            if "doy" in data.columns:
                st.line_chart(data.set_index("doy")[column])
            elif "year" in data.columns:
                st.line_chart(data.set_index("year")[column])
            else:
                st.line_chart(data[column])

        elif chart_type == "bar":

            if "year" in data.columns:
                yearly = data.groupby("year")[column].mean()
                st.bar_chart(yearly)
            else:
                st.bar_chart(data[column])

        elif chart_type == "histogram":
            st.bar_chart(data[column])
