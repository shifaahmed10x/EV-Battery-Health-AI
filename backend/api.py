from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load models
soh_model = joblib.load("models/soh_model.pkl")
anomaly_model = joblib.load("models/anomaly_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = np.array([
        data["Voltage_measured"],
        data["Current_measured"],
        data["Temperature_measured"],
        data["Current_charge"],
        data["Voltage_charge"]
    ]).reshape(1, -1)

    # Predictions
    soh = soh_model.predict(features)[0]
    anomaly = anomaly_model.predict(features)[0]

    status = "Normal"
    if soh < 60:
        status = "Critical"
    elif soh < 80:
        status = "Warning"
    MAX_LIFE = 1000  # assumed total usage units
    rul = (soh / 100) * MAX_LIFE

    return jsonify({
        "Battery_Health": round(float(soh), 2),
        "Status": status,
        "Anomaly": "Yes" if anomaly == -1 else "No",
        "Remaining_Useful_Life": int(rul)
    })
    

if __name__ == "__main__":
    app.run(debug=True)
