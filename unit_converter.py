import streamlit as st
from pint import UnitRegistry

# Initialize Unit Registry
ureg = UnitRegistry()
Q_ = ureg.Quantity

# Define unit categories and unit pairs
unit_categories = {
    "Area": ["square meter", "square foot", "square kilometer", "square mile", "acre", "hectare"],
    "Data Transfer Rate": ["bit/second", "kilobit/second", "megabit/second", "gigabit/second", "terabit/second"],
    "Digital Storage": ["byte", "kilobyte", "megabyte", "gigabyte", "terabyte"],
    "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt hour"],
    "Frequency": ["hertz", "kilohertz", "megahertz", "gigahertz"],
    "Fuel Economy": ["mile/gallon", "kilometer/liter", "liter/100 kilometer"],
    "Length": ["meter", "kilometer", "mile", "yard", "foot", "inch"],
    "Mass": ["gram", "kilogram", "pound", "ounce", "ton"],
    "Plane Angle": ["radian", "degree"],
    "Pressure": ["pascal", "bar", "psi", "atmosphere"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour", "knot"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day", "week"],
    "Volume": ["liter", "milliliter", "cubic meter", "gallon", "pint", "fluid ounce"]
}

# Styling
st.set_page_config(page_title="Advanced Unit Converter", layout="centered")
st.markdown("<h1 style='text-align: center;'>🌐 Advanced Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
category = st.selectbox("Select Unit Category", list(unit_categories.keys()))

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", unit_categories[category])
with col2:
    to_unit = st.selectbox("To", unit_categories[category])

value = st.number_input("Enter Value", value=0.0, format="%.6f")

convert_clicked = st.button("🔄 Convert")

def convert_units(value, from_u, to_u):
    try:
        quantity = Q_(value, from_u)
        converted = quantity.to(to_u)
        return f"{converted.magnitude:.6f} {converted.units}"
    except Exception as e:
        return f"❌ Conversion error: {str(e)}"

if convert_clicked:
    with st.spinner("Converting..."):
        result = convert_units(value, from_unit, to_unit)
        st.success(f"✅ Result: {value} {from_unit} = {result}")
