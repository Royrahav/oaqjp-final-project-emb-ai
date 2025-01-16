import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url=url, headers=header, json=payload)
    formatted_response = json.loads(response.text)

    if response.status_code == 500 or response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion= None
    else:
        emotions_dict = formatted_response['emotionPredictions'][0]['emotion']

        anger_score = emotions_dict['anger']
        disgust_score = emotions_dict['disgust']
        fear_score = emotions_dict['fear']
        joy_score = emotions_dict['joy']
        sadness_score = emotions_dict['sadness']

        dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    
    return {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score,'dominant_emotion': dominant_emotion}