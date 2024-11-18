import os
import pickle
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

# Define paths to model and vectorizer
base_dir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(base_dir, "model.pkl")
vectorizer_path = os.path.join(base_dir, "vectorizer.pkl")

# Load the model and vectorizer
try:
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    with open(vectorizer_path, 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
except Exception as e:
    raise RuntimeError(f"Error loading model/vectorizer: {e}")

@app.route('/')
def home():
    """Serve the homepage."""
    return send_from_directory('static', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests."""
    try:
        data = request.json  # Receive JSON data
        posts = data.get('posts', '')

        if not posts:
            return jsonify({'error': 'No input provided'}), 400

        # Transform input and make prediction
        input_vector = vectorizer.transform([posts])
        prediction = model.predict(input_vector)
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
