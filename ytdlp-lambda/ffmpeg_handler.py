import os
import subprocess


def handle_ffmpeg():
    if os.path.exists("/tmp/ffmpeg"):
        return True
    
    command = "cp /opt/python/bin/ffmpeg /tmp/ffmpeg; chmod 777 /tmp/ffmpeg"
    subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    
    return os.path.exists("/tmp/ffmpeg")