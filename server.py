"""
Flask server for emotion detection.
This module provides a web API endpoint to analyze emotions from text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Specify Flask
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_emotion():
    """Retrieve text from request and analyze emotions."""
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract dominant emotion
    dominant_emotion = response.pop('dominant_emotion', None)

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    # Extract emotions score
    emotions_str = ", ".join([f"'{key}': {value}" for key, value in response.items()])
    return (
        f"For the given statement, the system response is {emotions_str}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
