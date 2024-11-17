document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from reloading the page

    // Get the text input from the textarea
    const posts = document.getElementById('posts').value;

    // Prepare the data to send to the backend
    const data = { posts: posts };

    // Make the POST request to the Flask backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Show the result
        const resultDiv = document.getElementById('prediction-result');
        const resultText = document.getElementById('result-text');
        resultText.textContent = 'Predicted Personality: ' + data.prediction;
        resultDiv.style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
