import pickle
from flask import Flask, render_template, request, send_from_directory
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC  # Support Vector Classifier
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Load the pre-trained model and vectorizer
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
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
