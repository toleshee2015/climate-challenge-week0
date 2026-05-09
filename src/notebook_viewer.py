from pathlib import Path
import json
import streamlit as st


class NotebookViewer:

    NOTEBOOK_DIR = Path("notebooks")

    @staticmethod
    def get_notebooks():

        """
        Return all notebook files
        """

        if not NotebookViewer.NOTEBOOK_DIR.exists():
            return []

        return list(
            NotebookViewer.NOTEBOOK_DIR.glob("*.ipynb")
        )

    @staticmethod
    def load_notebook(notebook_path):

        """
        Load notebook JSON content
        """

        with open(notebook_path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def extract_markdown_cells(notebook_data):

        """
        Extract markdown cells only
        """

        markdown_cells = []

        for cell in notebook_data.get("cells", []):

            if cell.get("cell_type") == "markdown":

                markdown_cells.append(
                    "".join(cell.get("source", []))
                )

        return markdown_cells

    @staticmethod
    def display_notebook_info():

        st.subheader("📓 Notebook Integration")

        notebooks = NotebookViewer.get_notebooks()

        # No notebooks found
        if not notebooks:

            st.warning(
                "No notebooks found in the notebooks/ directory."
            )

            return

        # Notebook selector
        notebook_names = [
            notebook.name for notebook in notebooks
        ]

        selected_notebook = st.selectbox(
            "Select Notebook",
            notebook_names
        )

        # Selected notebook path
        notebook_path = next(
            notebook
            for notebook in notebooks
            if notebook.name == selected_notebook
        )

        # Load notebook
        notebook_data = NotebookViewer.load_notebook(
            notebook_path
        )

        # Notebook metadata
        st.markdown("### 📘 Notebook Details")

        st.write(
            {
                "Notebook": notebook_path.name,
                "Cells": len(
                    notebook_data.get("cells", [])
                ),
                "Kernel": notebook_data.get(
                    "metadata",
                    {}
                ).get(
                    "kernelspec",
                    {}
                ).get(
                    "display_name",
                    "Unknown"
                )
            }
        )

        # Markdown preview
        st.markdown("### 📝 Markdown Preview")

        markdown_cells = (
            NotebookViewer.extract_markdown_cells(
                notebook_data
            )
        )

        if markdown_cells:

            for cell in markdown_cells[:3]:

                st.markdown(cell)

        else:

            st.info(
                "No markdown cells found."
            )
