# Import library 
import requests
import json

'''
URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }
'''

# Create function for relevate emotion
def emotion_detector(text_to_analyse):

    # URL interate in task for generete request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    
    # Set the headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create a dict with text to analized
    text_to_analyse = { "raw_document": { "text": text_to_analyse } }

    # Response text analized from post request
    response = requests.post(url, json = text_to_analyse, headers = headers)

    # # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting sentiment : anger, disgust, fear, joy, sadness, and scores
    if response.status_code == 200:
        emotions = formatted_response["emotionPrediction"][0]["emotion"]

        # Compute the dominant emotion
        dom_emotion = max(emotions, key=emotions.get)

        # Add dominant emotion to the dictionary
        emotions["dominant_emotion"] = dom_emotion

    # Error not status code 200   
    elif response.status_code != 200:
        emotion = {"anger": None,
                   "disgust": None,
                   "fear": None,
                   "joy": None,
                   "sadness": None,
                   "dominant_emotion": None
                   }
        
    # Returning a dictionary containing sentiment analysis results
    return emotions
   
    
	