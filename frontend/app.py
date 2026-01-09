import streamlit as st
import requests

st.set_page_config(page_title="EV Battery Health Monitor", layout="centered")

st.title("🔋 EV Battery Health Monitoring System")

st.write("Enter battery parameters to predict health and detect anomalies.")

# Input fields
voltage_measured = st.number_input("Voltage Measured", value=4.0)
current_measured = st.number_input("Current Measured", value=1.0)
temperature_measured = st.number_input("Temperature Measured", value=30.0)
current_charge = st.number_input("Charging Current", value=1.5)
voltage_charge = st.number_input("Charging Voltage", value=4.2)

if st.button("Predict Battery Health"):
    payload = {
        "Voltage_measured": voltage_measured,
        "Current_measured": current_measured,
        "Temperature_measured": temperature_measured,
        "Current_charge": current_charge,
        "Voltage_charge": voltage_charge
    }

    try:
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json=payload
        )

        result = response.json()

        st.success(f"🔋 Battery Health: {result['Battery_Health']} %")
        st.info(f"📊 Status: {result['Status']}")
        st.warning(f"🚨 Anomaly Detected: {result['Anomaly']}")
        st.info(f"⏳ Remaining Useful Life: {result['Remaining_Useful_Life']} units")


    except Exception as e:
        st.error("Could not connect to backend API")
        st.write(e)
