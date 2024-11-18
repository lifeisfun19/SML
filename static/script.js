document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent page reload
    
    const posts = document.getElementById('posts').value;

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ posts })
    })
    .then(response => response.json())
    .then(data => {
        if (data.prediction) {
            document.getElementById('result-text').textContent = 'Predicted Personality: ' + data.prediction;
            document.getElementById('prediction-result').style.display = 'block';
        } else if (data.error) {
            console.error('Error:', data.error);
        }
    })
    .catch(error => console.error('Error:', error));
});
