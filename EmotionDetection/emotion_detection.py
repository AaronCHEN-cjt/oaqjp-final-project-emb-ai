import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=input_data)
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)  # This will help us understand the actual response structure
    # If the request is successful
    if response.status_code == 200:
        # Parse the response text as a JSON object
        response_json = response.json()

        emotions_data = response_json.get('emotionPredictions', [])
        
        if emotions_data:
            emotions = emotions_data[0].get('emotion', {})

            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)
            dominant_emotion = max(emotions, key=emotions.get)
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            return "No emotions detected in the response."
    
    # If the request fails, return the error message
    else:
        return f"Error: {response.status_code}, {response.text}"
