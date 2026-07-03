from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load("cow_health_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return "Cow Health Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    temperature = data["temperature"]
    activity = data["activity"]

    input_data = np.array([[temperature, activity]])
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    return jsonify({
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)