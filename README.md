<h1 align="center" style="font-weight: bold;">YVA - YouTube Video Analyser ▶️</h1>

<p align="center">
 <a href="#tech">Technologies</a> • 
 <a href="#started">Getting Started</a> • 

</p>

<p align="center">
    <b>Simple project to receive a video URL, transcribe, and summarize with AI Whisper.</b>
</p>

<h2 id="technologies">💻 Technologies</h2>

- Python
    - Libraries
        - PyTubeFix
        - StreamLit
        - Whisper (OpenAI)
        - Groq (LangChain)
        - FFMPEG

<h2 id="started">🚀 Getting started</h2>

You need enter in directory to install all dependencies (Libraries). Go to ```CMD``` inside of directory and run the codes below:

```bash
poetry install
poetry shell
```

<h3>Prerequisites</h3>

Necessary for running the project:

- [Python](https://python.org)
- [Poetry](https://python-poetry.org)

<h3>Cloning</h3>

How to clone the project

```bash
git clone https://github.com/EricRafael-Dev/YVA-Youtube_Video_Analyser
```

<h3>Config .env variables</h2>

Use the `.env.example` as reference to create your configuration file `.env` with your Groq Credentials

```yaml
GROQ_API_KEY = "your_groq_api"
```

<h3>Starting</h3>

How to start your project

```bash
streamlit run resume_yt_videos_project\__init__.py
```

<h3>Documentations that might help</h3>

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)