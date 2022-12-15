import json
import os
import base64
from urllib import request
from slack_handler import send_message

def lambda_handler(event, context):
    
    print(event)
    
    # to respond with 'challenge' from slack
    try:
        if json.loads(event['body'])['challenge']:
            return {
                "statusCode": 200,
                'body': json.loads(event['body'])['challenge']
            }
    except:
        pass
    
    for ev in event['Records']:
        payload = ev['body']
        ll = base64.b64decode(payload).decode('utf-8').split('&')
        
        payload = {}
        for i in ll:
            k, v = i.split('=')
            payload[k] = v
            
        response = request.urlopen(os.environ['ytdlp_lambda_api'] + "?youtube-url=" + payload['text'])
        response = json.loads(response.read().decode('utf-8'))
        
        send_message(payload, response['signed_url'], response['info'])

    return {
        'statusCode': 200,
        'body': "Success"
    }
