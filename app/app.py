from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('app/model.pkl')
scaler = joblib.load('app/scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=False)  # Ensure debug mode is off in production
