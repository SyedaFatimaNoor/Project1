import streamlit as st

# Page configuration
st.set_page_config(
    page_title="📊 Unit Converter Pro",
    page_icon="📊",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main {
        max-width: 800px;
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background: linear-gradient(135deg, #6e8efb, #a777e3);
        color: white;
        font-weight: bold;
    }
    .stSelectbox div[data-baseweb="select"] {
        margin-bottom: 1rem;
    }
    .result-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 1.5rem;
        margin-top: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    @media (prefers-color-scheme: dark) {
        .result-box {
            background-color: #2d3748;
        }
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("📊 Unit Converter Pro")
st.write("Convert between different units easily!")

# Conversion types with more categories and units
conversion_types = {
    "📏 Length": {
        "units": ["meter (m)", "kilometer (km)", "mile (mi)", "yard (yd)", "foot (ft)", "inch (in)"],
        "conversion": {
            "meter (m)": 1,
            "kilometer (km)": 1000,
            "mile (mi)": 1609.34,
            "yard (yd)": 0.9144,
            "foot (ft)": 0.3048,
            "inch (in)": 0.0254
        }
    },
    "📰 Weight": {
        "units": ["gram (g)", "kilogram (kg)", "pound (lb)", "ounce (oz)", "ton (t)"],
        "conversion": {
            "gram (g)": 1,
            "kilogram (kg)": 1000,
            "pound (lb)": 453.592,
            "ounce (oz)": 28.3495,
            "ton (t)": 1000000
        }
    },
    "💧 Volume": {
        "units": ["liter (L)", "milliliter (mL)", "gallon (gal)", "quart (qt)", "pint (pt)", "cup"],
        "conversion": {
            "liter (L)": 1,
            "milliliter (mL)": 0.001,
            "gallon (gal)": 3.78541,
            "quart (qt)": 0.946353,
            "pint (pt)": 0.473176,
            "cup": 0.24
        }
    },
    "🔥 Temperature": {
        "units": ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"],
        "special_case": "temperature"
    }
}

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    # Category selection
    category = st.selectbox("Select category", list(conversion_types.keys()))
    
    # Get units based on selected category
    units = conversion_types[category]["units"]
    
    # Input value
    value = st.number_input("Enter value", min_value=0.0, value=1.0, step=0.01, format="%.4f")

with col2:
    # From and To unit selection
    from_unit = st.selectbox("From", units, index=0)
    to_unit = st.selectbox("To", units, index=1)

# Convert button with emoji
convert_btn = st.button("➡️ Convert", type="primary")

# Conversion logic
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    # First convert to Celsius
    if from_unit == "Celsius (°C)":
        celsius = value
    elif from_unit == "Fahrenheit (°F)":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin (K)":
        celsius = value - 273.15
    
    # Convert from Celsius to target unit
    if to_unit == "Celsius (°C)":
        return celsius
    elif to_unit == "Fahrenheit (°F)":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin (K)":
        return celsius + 273.15

# Handle conversion when button is clicked
if convert_btn and value is not None:
    try:
        if category == "🔥 Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        else:
            # Standard conversion for other categories
            base_value = value * conversion_types[category]["conversion"][from_unit]
            result = base_value / conversion_types[category]["conversion"][to_unit]
        
        # Display result in a nice box
        st.markdown(f"""
        <div class="result-box">
            <h3>Result</h3>
            <p style="font-size: 24px; margin: 0;">
                {value} {from_unit.split(' (')[0]} = 
                <span style="color: #6e8efb; font-weight: bold;">
                    {result:.4f} {to_unit.split(' (')[0]}
                </span>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error("An error occurred during conversion. Please check your inputs.")

# Add some space at the bottom
st.write("")
st.write("---")
st.caption("Created with ❤️ using Streamlit")

# Add a reset button
if st.button("🔄 Reset"):
    st.experimental_rerun()
