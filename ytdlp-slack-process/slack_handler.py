import os
import logging
import json
from slack_sdk import WebClient

logging.basicConfig(level=logging.DEBUG)

bot_user_oath_token = os.environ['bot_user_oath_token']

slack_token = bot_user_oath_token
client = WebClient(token=bot_user_oath_token)

def get_block(payload, s3_url, info):
    return  [
					{
						"type": "section",
						"text": {
							"type": "mrkdwn",
							"text": f"Your file [{info['title']}] is ready for download. \n\n "
						}
					},
					{
						"type": "divider"
					},
					{
						"type": "section",
						"text": {
							"type": "mrkdwn",
							"text": "Click the button to download."
						},
						"accessory": {
							"type": "button",
							"text": {
								"type": "plain_text",
								"text": "Download"
							},
						"value": "click_me_123",
						"url": s3_url,
						"action_id": "button-action"
						}
					}
				]



def send_message(payload, s3_url, info):

    response = client.conversations_open(
    	users=[payload['user_id']]
    	)
    	
    channel_id = response.data['channel']['id']
    
    client.chat_postMessage(
    	channel=channel_id, 
    	blocks=get_block(payload, s3_url, info)
    	)