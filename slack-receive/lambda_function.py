import os
import json
import base64
import boto3
from datetime import datetime

def lambda_handler(event, context):

    # Get the service resource
    sqs = boto3.client('sqs')

    # Create a new message
    response = sqs.send_message(
        QueueUrl=os.environ['queue_url'],
        MessageBody=event['body']
        )

    return {
        "statusCode": 200,
        "body": "mp3fy request received."
    }
