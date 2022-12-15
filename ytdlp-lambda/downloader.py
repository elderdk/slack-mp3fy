from option_maker import get_options
from yt_dlp import YoutubeDL

def download(url, preferred_codec):

    filename, options, info = get_options(url, preferred_codec)
    print(options)
    with YoutubeDL(options) as ydl:
        ydl.download(url)

    return filename, info