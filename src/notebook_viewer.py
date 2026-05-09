import streamlit as st


class NotebookViewer:

    @staticmethod
    def display_notebook_info():

        st.info(
            """
            📘 Jupyter Notebook Integration

            Available notebooks:

            - climate_analysis.ipynb
            - forecasting.ipynb
            - anomaly_detection.ipynb

            Future improvement:
            Direct notebook rendering inside Streamlit.
            """
        )
