import streamlit as st


class NotebookViewer:

    @staticmethod
    def display_notebook_info():

        st.info(
            """
            Jupyter Notebook Integration

            You can integrate:
            - climate_analysis.ipynb
            - forecasting.ipynb
            - anomaly_detection.ipynb

            Future improvement:
            Render notebook outputs directly inside Streamlit.
            """
        )
