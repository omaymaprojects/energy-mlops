from flask import Flask, request, jsonify
import joblib
import numpy as np
app = Flask(__name__)
model = joblib.load('model.pkl')
preprocessor = joblib.load('preprocessor.pkl')
@app.route('/predict', methods=['POST'])
def predict():
    data = requet.get_json()
    features = np.array(data['features']).reshape(1, -1)
    features =  preprocessor.transform(features)
    prediction = model.predict(features)
    return jsonify({'prediction':prediction.tolist()})
if __name__=='__main__':
    app.run(debug=True)
