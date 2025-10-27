import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction App")

# User input fields
area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, value=2000)
bed = st.number_input("Bedrooms", 1, 10, 3)
bath = st.number_input("Bathrooms", 1, 10, 2)
floors = st.number_input("Floors", 1, 5, 2)
year = st.number_input("Year Built", 1900, 2025, 2018)
garage = st.selectbox("Garage", ['Yes', 'No'])
location = st.selectbox("Location", ['Rural', 'Suburban', 'Urban'])
condition = st.selectbox("Condition", ['Poor', 'Fair', 'Good'])

# Convert user input to model format
data = {
    'Area': [area],
    'Bedrooms': [bed],
    'Bathrooms': [bath],
    'Floors': [floors],
    'YearBuilt': [year],
    'Garage': [1 if garage == 'Yes' else 0],
    'Location_Rural': [1 if location == 'Rural' else 0],
    'Location_Suburban': [1 if location == 'Suburban' else 0],
    'Location_Urban': [1 if location == 'Urban' else 0],
    'Condition_Fair': [1 if condition == 'Fair' else 0],
    'Condition_Good': [1 if condition == 'Good' else 0],
    'Condition_Poor': [1 if condition == 'Poor' else 0],
}

df = pd.DataFrame(data)

# Predict button
if st.button("Predict Price"):
    price = model.predict(df)[0]
    st.success(f"Predicted House Price: ₹{price:,.2f}")
