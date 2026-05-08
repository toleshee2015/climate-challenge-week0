import pandas as pd
from pathlib import Path

class DataLoader:
    @staticmethod
    def load_data():
        # This locates the folder containing your script
        BASE_DIR = Path(__file__).resolve().parent.parent
        
        # Ensure 'ethiopia.csv' is the EXACT name of your file in the /data folder
        file_path = BASE_DIR / "data" / "ethiopia.csv"
        
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            # This helps you debug if the path is still wrong
            import streamlit as st
            st.error(f"File not found at: {file_path}")
            return None
