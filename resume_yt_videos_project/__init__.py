from pytubefix import YouTube
import subprocess

"""
    Convert a video file MP4 to MP3 using ffmpeg
"""

yt = YouTube('https://www.youtube.com/shorts/7fTHD07Q9Pw')

stream = yt.streams[0].url

def convert_video_to_mp3(input, output):

    try:
        # Comand FFmpeg
        command = [
            "PATH/ffmpeg", "-i", input, 
            "-vn", "-ar", "44100", 
            "-ac", "2", "-b:a", "192k", 
            output
        ]
        
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Conversion completed: {output}")

    except subprocess.CalledProcessError as e:
        print("Error converting file:", e)

    except FileNotFoundError:
        print("FFmpeg isn't installed or isn't at PATH.")

# Exemplo de uso
convert_video_to_mp3(stream, "audio.mp3")
 