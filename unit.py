import streamlit as st

# Page configuration
st.set_page_config(page_title="Unit Converter")

# Length conversion function
def length_conversion(value, from_unit, to_unit):
    conversion_factors = {
        "Centimeter": 1,
        "Meters": 0.01,
        "Kilometers": 0.001,
        "Feet": 0.0328084,
        "Inches": 0.393701
    }

    # Convert to centimeters first
    value_in_cm = value / conversion_factors[from_unit]
    converted_value = value_in_cm * conversion_factors[to_unit]
    return converted_value
#weight Conversion 
def weight_conversion(value, from_unit, to_unit):
    con_factor = {
        "gram": 1,
        "kilogram": 0.001,
        "pounds" : 453.592
    }
    
    value_in_cm = value / con_factor[from_unit]
    converted_value = value_in_cm * con_factor[to_unit]
    return converted_value
    

# App Title
st.title("Unit Converter")
st.write("Convert between different units of measurement easily!")

# Sidebar
st.sidebar.title("Unit Converter")
st.sidebar.write("Welcome to the Unit Converter!")
st.sidebar.write("Select the conversion type and enter the value you want to convert.")

# Conversion Type
conversion_type = st.selectbox("Choose a conversion type", ["Length", "Weight"])

# Length Conversion Section
if conversion_type == "Length":
    st.header("Length Conversion")

    length_units = ["Centimeter", "Meters", "Kilometers", "Feet", "Inches"]
    from_unit = st.selectbox("From Unit", length_units)
    to_unit = st.selectbox("To Unit", length_units)
    input_value = st.number_input("Enter the value to convert:", min_value=0.0, format="%.2f")

    if st.button("Convert"):
        result = length_conversion(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} is equal to {result:.2f} {to_unit}")
    else:
        st.info("Click the button to perform the conversion.")

# Weight Conversion Placeholder
if conversion_type == "Weight":
    st.header("Weight Conversion")
    Weight_units = ["gram","kilogram","pounds"]
    from_unit = st.selectbox("From Unit", Weight_units)
    to_unit = st.selectbox("To Unit", Weight_units)
    input_value = st.number_input("Enter the value to convert:", min_value=0.0, format="%.2f")

    if st.button("Convert"):
        result = weight_conversion(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} is equal to {result:.2f} {to_unit}")
    else:
        st.info("Click the button to perform the conversion.")



# Footer
st.markdown("---")
st.write("Thank you for using the Unit Converter!")
