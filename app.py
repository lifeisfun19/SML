from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/style.css')
def serve_css():
    return send_from_directory('.', 'style.css')  # Adjust path if needed

@app.route('/script.js')
def serve_js():
    return send_from_directory('.', 'script.js')

# Load the trained model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')


# Prediction route for the model
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get the JSON data
    text = data['posts']  # Assuming input is passed under the key 'posts'
    
    # Vectorize the input text
    text_vect = vectorizer.transform([text])
    
    # Predict the personality type
    prediction = model.predict(text_vect)
    
    return jsonify({'prediction': prediction[0]})  # Return the predicted type

if __name__ == '__main__':
    app.run(debug=True)
