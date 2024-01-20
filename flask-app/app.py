from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS

# Load the trained model
model = joblib.load('../iris_model.pkl')

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [float(i) for i in data['features']]
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
