import pickle
from flask import Flask, render_template, request, jsonify
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
    return render_template('index.html')  # Render index.html from templates folder

@app.route('/predict', methods=['POST'])
def predict():
    # Get the text from the form in index.html
    posts = request.form['posts']  # assuming 'posts' is the name attribute in the form
    
    # Vectorize the input text
    input_vector = vectorizer.transform([posts])
    
    # Make the prediction
    prediction = model.predict(input_vector)
    
    # Return the result as a JSON response or render it in HTML
    return jsonify({'prediction': prediction[0]})  # For JSON response

if __name__ == '__main__':
    app.run(debug=True)
