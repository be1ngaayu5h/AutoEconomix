import streamlit as st
import joblib
import pandas as pd
import datetime

st.set_page_config(page_title="AutoEconomix", layout="centered")

st.title("🚗 AutoEconomix")
st.subheader("Used Car Price Predictor")

# Load dataset
df_raw = pd.read_csv("data/cars.csv")

# Recreate feature engineering (same as training)
df_raw['brand'] = df_raw['car_name'].str.split(n=1).str[0]
df_raw['model'] = df_raw['car_name'].str.split().str[1:4].str.join(' ')

current_year = datetime.datetime.now().year
df_raw['age'] = current_year - df_raw['year_of_manufacture']

# Load trained model
model = joblib.load("model/CarRandomForestRegressor.pkl")

st.markdown("### Enter Car Details")

brand = st.selectbox("Brand", sorted(df_raw["brand"].unique()))
model_name = st.selectbox("Model", sorted(df_raw["model"].unique()))
fuel_type = st.selectbox("Fuel Type", sorted(df_raw["fuel_type"].unique()))
city = st.selectbox("City", sorted(df_raw["city"].unique()))

kms_driven = st.number_input("Kilometers Driven", min_value=0)
age = st.number_input("Age (Years)", min_value=0)

if st.button("Predict Price"):
    input_df = pd.DataFrame({
        "brand": [brand],
        "model": [model_name],
        "kms_driven": [kms_driven],
        "fuel_type": [fuel_type],
        "city": [city],
        "age": [age]
    })

    prediction = model.predict(input_df)

    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")
