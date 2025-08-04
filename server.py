from flask_cors import CORS
from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

# Initialize Flask application
app = Flask(__name__)
CORS(app)

# Define the route for the emotion detector (accept GET requests)
@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    # Get the text from the user input
    text_to_analyze = request.args.get('textToAnalyze')  # Use request.args to get GET parameters
    
    # Get emotion analysis result
    result = emotion_detector(text_to_analyze)
    
    # Return the result as JSON
    return jsonify(result)

# Define the home route that renders the index.html
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask app on localhost at port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
