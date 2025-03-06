import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze): 
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    #print(formatted_response)

    
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Extract elements
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        full_response = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
        }
    # If the response status code is 400, set label and score to None
    elif response.status_code == 400:
        full_response = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None 
    }  
    # Format
    return full_response