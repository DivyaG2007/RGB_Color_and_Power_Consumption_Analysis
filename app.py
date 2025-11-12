import streamlit as st
import joblib
import numpy as np

# Load trained model and scaler
model = joblib.load("power_predictor.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🎨 Power Consumption Predictor from RGB Values")

r = st.slider("R (0-255)", 0, 255, 100)
g = st.slider("G (0-255)", 0, 255, 100)
b = st.slider("B (0-255)", 0, 255, 100)
brightness = st.number_input("Original Brightness", min_value=0.0, max_value=300.0, value=150.0)
lux = st.number_input("Ambient Lux", min_value=0, max_value=100, value=20)
temp = st.number_input("Temperature (°C)", min_value=10, max_value=50, value=25)

if st.button("Predict Power Usage"):
    input_data = np.array([[r, g, b, brightness, lux, temp]])
    scaled = scaler.transform(input_data)
    pred = model.predict(scaled)[0]
    st.success(f"🔋 Estimated Power Consumption: {pred:.2f} W")
