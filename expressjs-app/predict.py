import sys
import json
import joblib

# Load the trained model (update the path if necessary)
model = joblib.load('../iris_model.pkl')

# Convert input string back to a list (and then to the format your model needs)
features = json.loads(sys.argv[1])

# Make a prediction
prediction = model.predict([features])

# Output the prediction
print(prediction[0])
