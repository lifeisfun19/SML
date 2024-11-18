import pickle
from flask import Flask, render_template, request, send_from_directory
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC  # Support Vector Classifier
from sklearn.metrics import accuracy_score

app = Flask(__name__)

import os  # Add this import for handling paths

# Specify the absolute path to the files
model_path = r"C:\Users\LENOVO\my_project\model.pkl"
vectorizer_path = r"C:\Users\LENOVO\Desktop\vectorizer.pkl"

base_dir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(base_dir, "model.pkl")


with open(vectorizer_path, 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    # Serve the index.html from the static folder
    return send_from_directory('static', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Receive JSON data
        posts = data.get('posts', '')
        input_vector = vectorizer.transform([posts])
        prediction = model.predict(input_vector)
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
