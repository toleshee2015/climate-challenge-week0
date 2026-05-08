# -----------------------------
# Load Dataset
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "ethiopia.csv"

data = pd.read_csv(file_path)

# -----------------------------
# Dataset Info (NEW: User-friendly lists)
# -----------------------------
st.subheader("📌 Available Data Overview")

if "country" in data.columns:
    countries_list = sorted(data["country"].unique())
    st.markdown("### 🌍 Available Countries")
    st.write(countries_list)

numeric_columns = data.select_dtypes(include=["number"]).columns.tolist()

st.markdown("### 📊 Available Indicators")
st.write(numeric_columns)
# -----------------------------
# Sidebar - Country Comparison
# -----------------------------
st.sidebar.header("🌍 Country Comparison")

if "country" in data.columns:
    countries = sorted(data["country"].unique())

    selected_countries = st.sidebar.multiselect(
        "Select countries to analyze",
        countries,
        default=countries[:2] if len(countries) >= 2 else countries,
        help="Choose one or more countries for comparison"
    )

    filtered_data = data[data["country"].isin(selected_countries)]
else:
    st.sidebar.warning("No country column found.")
    filtered_data = data

# -----------------------------
# Sidebar - Indicator Selection
# -----------------------------
st.sidebar.header("📊 Indicator Selection")

numeric_columns = filtered_data.select_dtypes(include=["number"]).columns.tolist()

selected_column = st.sidebar.selectbox(
    "Select climate variable",
    numeric_columns,
    help="Choose temperature, rainfall, or other indicators"
)
# -----------------------------
# Data Description
# -----------------------------
st.subheader("ℹ Dataset Description")

st.info("""
This dashboard allows users to explore climate data across African countries.

### Users can:
- Select countries from the available list
- Analyze temperature, rainfall, and other indicators
- Compare trends across regions
- Visualize patterns interactively

### Available Data:
- Countries: displayed above
- Indicators: numeric climate variables (e.g., temperature, rainfall)
""")
