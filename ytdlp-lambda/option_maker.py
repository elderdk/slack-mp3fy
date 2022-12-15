from yt_dlp import YoutubeDL

def get_options(url, preferred_codec):
    
    options = {
        
        'noplaylist': True,
        'quiet': True,
        'format': 'm4a/bestaudio/best',
        'ffmpeg_location': '/tmp/ffmpeg',

        
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': preferred_codec,
                
        }]
    }

    with YoutubeDL(options) as ydl:        
        info = ydl.extract_info(url, download=False)
    
    filename = "/tmp/" + info.get('title') + '.' + preferred_codec
    
   
    options['outtmpl'] = {'default': filename}
    
    return filename, options, info