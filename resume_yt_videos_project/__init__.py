import pytubefix
import subprocess
import pytubefix.exceptions
import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

command_whisper_install = [
            "pip", "install", "openai-whisper"
        ]
subprocess.run(command_whisper_install, check=True)

import whisper
    #Convert a video file MP4 to MP3 using ffmpeg


def go(input=""):

    #Taking a URL video to convert

    try:
        yt = pytubefix.YouTube(input)

        try:
            os.mkdir('media')
        except FileExistsError:
            pass
            
        filename = f'media\{yt.title.replace(" ","_")+".mp3"}'

        stream = yt.streams[0].url

        st.text(yt.title)
        convert_video_to_mp3(stream, filename) 

    

    except pytubefix.exceptions.RegexMatchError:
        st.warning("Put a YouTube Link!")

    except TypeError:
        st.warning("Put a YouTube Link!")
    

def convert_video_to_mp3(input, output):

    try:
        # Comand FFmpeg and openai-whisper
        command = [
            "resume_yt_videos_project/PATH/ffmpeg", "-i", input, 
            "-vn", "-ar", "44100", 
            "-ac", "2", "-b:a", "192k", 
            output
        ]

        # Execute the command
        subprocess.run(command, check=True)
        print(f"Conversion completed: {output}")

        model = whisper.load_model("base")
        result = model.transcribe(output)
        
        resume = resume_transcribe_AI(result["text"])
        st.text(resume.content)

        print('Resume completed')

        #deleting the mp3 file

        os.remove(output)

    except subprocess.CalledProcessError as e:
        print("Error converting file:", e)

    except FileNotFoundError:
        print("FFmpeg isn't installed or isn't at PATH.")

def resume_transcribe_AI(result):

    load_dotenv()

    api_key = os.environ['GROQ_API_KEY']

    client =Groq(
        api_key = api_key
    )
    
    response = client.chat.completions.create(

        messages = [
            {
            "role": "system",
            "content": """
            Você é um assistente que resume vídeos detalhadamente.
            Responda com formatação Markdown"""
        }, {
            "role": "user",
            "content": f"Descreva o seguinte vídeo: {result}"
        }
        ],
        model = "llama3-8b-8192"
    )
    return response.choices[0].message

# Calling the func    

input = st.text_input("Cole o link aqui: ")
go(input)
