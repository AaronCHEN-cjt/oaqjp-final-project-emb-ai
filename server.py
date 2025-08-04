"""
Flask server application for emotion detection.

This module sets up a simple Flask app with an endpoint to receive
text input, process the emotion analysis, and return the detected
emotion or error message.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Handles the emotion detection request and returns the emotion analysis result
    or an error message.

    The function receives the user's input text, processes it through the emotion
    detection function, and returns the detected emotion or an error message if the
    input is invalid.

    Returns:
        JSON response with the emotion analysis result or an error message.
    """
    text = request.json.get('textToAnalyze', "")
    result = emotion_detector(text)

    # Check if dominant emotion is None
    if result.get("emotion") is None:
        return jsonify({"error": "Invalid message! Please input again!"}), 400

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
