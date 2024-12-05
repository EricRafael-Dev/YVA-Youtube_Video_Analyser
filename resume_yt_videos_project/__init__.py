import pytubefix
import subprocess
import pytubefix.exceptions
import whisper
import streamlit as st
import os


    #Convert a video file MP4 to MP3 using ffmpeg


def go(input=""):

    #Taking a URL video to convert

    try:
        yt = pytubefix.YouTube(input)
    
        filename = yt.title.replace(" ","_")+".mp3"
        stream = yt.streams[0].url

        st.text(yt.title)
        convert_video_to_mp3(stream, filename) 

    except pytubefix.exceptions.RegexMatchError:
        st.warning("Put a YouTube Link!")

    except TypeError:
        st.warning("Put a YouTube Link!")
    


def convert_video_to_mp3(input, output):

    try:
        # Comand FFmpeg
        command = [
            "resume_yt_videos_project/PATH/ffmpeg", "-i", input, 
            "-vn", "-ar", "44100", 
            "-ac", "2", "-b:a", "192k", 
            output
        ]
        print()
        
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Conversion completed: {output}")

        model = whisper.load_model("base")
        result = model.transcribe(output)
        st.text(result["text"])

    except subprocess.CalledProcessError as e:
        print("Error converting file:", e)

    except FileNotFoundError:
        print("FFmpeg isn't installed or isn't at PATH." + os.listdir())

# Calling the func    

input = st.text_input("Cole o link aqui: ")
go(input)
