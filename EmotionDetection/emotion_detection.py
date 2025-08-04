import requests

def emotion_detector(text_to_analyze):
    # Check if the input is empty
    if not text_to_analyze.strip():
        return {"emotionPredictions": [{"emotion": {key: None for key in ["anger", "disgust", "fear", "joy", "sadness"]}}]}
    
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
    
    if response.status_code == 400:
        # For status code 400, return a dictionary with None values for all emotions
        return {"emotionPredictions": [{"emotion": {key: None for key in ["anger", "disgust", "fear", "joy", "sadness"]}}]}
    
    if response.status_code == 200:
        # If successful, parse and return emotions
        response_json = response.json()
        emotions_data = response_json.get('emotionPredictions', [])
        
        if emotions_data:
            emotions = emotions_data[0].get('emotion', {})
            return emotions
    else:
        return {"error": "Failed to retrieve emotions, please try again later."}
