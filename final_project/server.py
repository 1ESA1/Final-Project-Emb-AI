# Import Flask for creating the server
from flask import Flask,render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

"""
This file sets up a Flask server to handle requests for emotion detection.
It imports the necessary libraries and initializes the Flask app.
It also defines a route for the root URL that renders the index.html template.
"""
# Initialize Flask app
app = Flask("EmotionDetectorServer")

# Define route for the root URL
@app.route('/')
def render_index_page():
    """
    Render the index.html template when the root URL is accessed.
    """
    return render_template('index.html')

# Define route for emotion detection
@app.get("/emotionDetector")
def emotion_analyzer():
    """
    Handle GET requests to the /emotionDetector endpoint.
    It retrieves the text from the request, processes it using the emotion_detector,
    and returns the detected emotion as a JSON response.
    """
    # Get the text from the request
    text_to_analyze = request.args.get('textToAnalyze')
 
    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # Check if the result is None or dominant emotion is None
    if result is None or result['dominant_emotion'] is None:
        return "Invalid text! No emotion detected"

    # Return success response with the detected emotion
    return (
        f"For the given statement, the system detected: "
        f"anger: {result['anger']}, "
        f"disgust: {result['disgust']}, "
        f"fear: {result['fear']}, " 
        f"joy: {result['joy']}, "
        f"sadness: {result['sadness']}, "
        f"The dominant emotion is {result['dominant_emotion']}."
    ), 200

# Run the Flask app
if __name__ == "__main__":
    """
    Start the Flask server if this script is run directly.
    """
    app.run(host='0.0.0.0', port=5000, debug=True) # Note: The debug mode is enabled for development purposes.