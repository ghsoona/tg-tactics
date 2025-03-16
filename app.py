from flask import Flask, request, jsonify
import numpy as np
import joblib  # Make sure "injury_model.pkl" exists

app = Flask(__name__)

# Load the trained model
model = joblib.load("injury_model.pkl")

@app.route('/')
def home():
    return "T&G Tactics API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({"injury_risk": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

