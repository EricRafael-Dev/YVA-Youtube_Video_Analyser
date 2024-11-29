from pytubefix import YouTube
import subprocess
import whisper
"""
    Convert a video file MP4 to MP3 using ffmpeg
"""
filename = "transcript.mp3"
yt = YouTube('https://youtu.be/V1PNrhV9qjA?si=vE_ClB3X61J8s6Bl')

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

# Calling the func
convert_video_to_mp3(stream, filename)


model = whisper.load_model("tiny")
audio = whisper.load_audio(file="transcript.mp3")
transcript = model.transcribe('transcript.mp3')
print(transcript["text"])
