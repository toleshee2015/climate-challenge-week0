🌍 Ethiopia Climate Dashboard
📌 Overview

The Ethiopia Climate Dashboard is an interactive Streamlit application designed to explore and visualize climate-related data simply and intuitively.
It enables users to perform exploratory data analysis through interactive controls, dynamic filtering, and real-time visualizations.

🚀 Live Demo

👉 Try the app here:
(https://climate-challenge-week0-4a2zeeu5fdyzqmy8jvpfys.streamlit.app/)
🖼️ Preview

Dashboard Overview
✨ Features
Interactive exploration of climate data
Dynamic selection of variables
Multiple visualization types:
-->Line Chart
-->Bar Chart
-->Area Chart

📊 Dataset

The dataset (ethiopia.csv) contains structured climate observations for Ethiopia, including environmental indicators such as temperature and rainfall.
It is used for demonstrating exploratory data analysis and interactive visualization techniques.
🧠 Key Functionalities
-->Data Overview
-->Dataset dimensions (rows & columns)
-->Column listing
-->Data preview
-->Interactive Controls

Users can:
Select variables for analysis
Choose chart types
Adjust the number of rows displayed
Statistical Analysis
Mean
Standard deviation
Min/Max values
🛠️ Tech Stack
Python
Streamlit
Pandas
Pathlib
📁 Project Structure
climate-challenge-week0/
│
├── app/
│   └── main.py
│
├── data/
│   └── ethiopia.csv
│
├── assets/
│   ├── dashboard.png
│   └── chart.png
│
├── requirements.txt
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/toleshee2015/climate-challenge-week0.git
cd climate-challenge-week0
2. Install dependencies
pip install -r requirements.txt
3. Run the app
streamlit run app/main.py
☁️ Deployment
Deployed using Streamlit Community Cloud.
Requirements:

Entry file: app/main.py
Dataset included in data/
Dependencies in requirements.txt
📌 Future Improvements
-->Machine learning-based climate predictions
-->Time-series trend analysis
-->Geographic map visualizations
-->Export/download analysis results
-->Improved UI themes and dark mode toggle

## Author
Almaz Kisi Gonfa | Women in Tech Program – Paper Airplanes | 2026
