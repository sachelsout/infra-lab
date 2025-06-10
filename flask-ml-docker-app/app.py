# imports
import pickle
import numpy as np
from flask import Flask, request, jsonify

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the ML Model API!"

# Map class index to species
species = ["setosa", "versicolor", "virginica"]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    
    # Example input format: {"features": [5.1, 3.5, 1.4, 0.2]}
    features = np.array(data['features']).reshape(1, -1)
    if features is None:
        return jsonify({"error": "Missing 'features' in request"}), 400

    try:
        prediction = model.predict(features)[0]
        species_name = species[prediction]
        return jsonify({"prediction": species_name})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
