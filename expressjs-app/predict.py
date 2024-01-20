import sys
import json
import joblib

# Load the trained model
model = joblib.load('../iris_model.pkl')

# Read features from arguments
print("running script to predict")
features = json.loads(sys.argv[1])
features = [float(i) for i in features]
# Make a prediction
prediction = model.predict([features])
print(int(prediction[0]))
