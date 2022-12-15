import json
from ffmpeg_handler import handle_ffmpeg
from downloader import download
from boto3_handler import upload


def lambda_handler(event, context):
    
    print(event)

    ffmpeg_ready = handle_ffmpeg()
    
    if ffmpeg_ready is True:
        pass
    else:
        return "ffmpeg handle failed."
        
    url = event['queryStringParameters']['youtube-url']
    preferred_codec = 'mp3'

    filename, info = download(url, preferred_codec)
    signed_url = upload(filename)

    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'signed_url': signed_url,
            'info': info
        })
            
    }
