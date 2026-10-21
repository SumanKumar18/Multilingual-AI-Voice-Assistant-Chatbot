# 🎙️ Multilingual AI Voice Assistant

<p align="center">
  <b>An AI-Powered Voice Assistant for Speech Recognition, Multilingual Translation, and Voice Responses</b>
</p>

<p align="center">
  🐍 Python • 🎤 OpenAI Whisper • 🦙 Ollama • 🌐 Streamlit • 🗣️ Text-to-Speech
</p>

---

## 📌 Project Overview

The **Multilingual AI Voice Assistant** is a Python-based application designed to enable users to interact with an AI assistant through voice input.

The application uses **OpenAI Whisper** for speech-to-text transcription, language detection and translation tools for multilingual processing, **Ollama** for locally running a language model, and text-to-speech technology to generate spoken responses.

The user interface is built using **Streamlit**, providing a simple and interactive way to record audio and interact with the assistant.

The project explores how speech recognition, natural language processing, large language models, translation, and speech synthesis can work together in a single AI application.

---

## 🎯 Project Objectives

- 🎤 Convert spoken audio into text using OpenAI Whisper.
- 🌍 Support multilingual interaction through language detection and translation.
- 🧠 Generate AI-powered responses using a language model running through Ollama.
- 🔊 Convert text responses into speech.
- 💻 Build an interactive web interface using Streamlit.
- 🔗 Integrate multiple AI and NLP technologies into one application.
- 🔒 Explore local language-model inference using Ollama.

---

## ✨ Key Features

### 🎤 Speech Recognition
Uses OpenAI Whisper to transcribe recorded audio into text.

### 🌐 Multilingual Processing
Uses language detection and translation libraries to help process input across supported languages.

### 🧠 AI-Powered Responses
Integrates Ollama with a locally running language model to generate responses to user queries.

### 🔊 Text-to-Speech
Uses Google Text-to-Speech (gTTS) to convert generated text into spoken audio.

### 💻 Interactive User Interface
Uses Streamlit to provide a browser-based interface for interacting with the assistant.

### ⚡ Integrated AI Workflow
Combines speech recognition, language processing, AI response generation, and speech synthesis into a unified application.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🎙️ OpenAI Whisper | Speech-to-text transcription |
| 🦙 Ollama | Local language-model execution |
| 🧠 Llama 3.2 | Language model used through Ollama |
| 💻 Streamlit | Interactive web interface |
| 🌐 Deep Translator | Translation functionality |
| 🔎 Langdetect | Language detection |
| 🔊 gTTS | Text-to-speech generation |
| 🎤 Audio Recorder Streamlit | Audio recording through the interface |
| 🎵 FFmpeg | Audio processing support |

---

## ⚙️ System Architecture

The application follows a voice-to-response workflow.

```text
       ┌─────────────────────────┐
       │       User Input        │
       │     🎤 Voice Audio      │
       └────────────┬────────────┘
                    │
                    ▼
       ┌─────────────────────────┐
       │     Streamlit UI        │
       │   Audio Recording       │
       └────────────┬────────────┘
                    │
                    ▼
       ┌─────────────────────────┐
       │    OpenAI Whisper       │
       │    Speech-to-Text       │
       └────────────┬────────────┘
                    │
                    ▼
       ┌─────────────────────────┐
       │ Language Detection and  │
       │ Translation Processing  │
       └────────────┬────────────┘
                    │
                    ▼
       ┌─────────────────────────┐
       │    Ollama + Llama 3.2   │
       │   AI Response Generation│
       └────────────┬────────────┘
                    │
                    ▼
       ┌─────────────────────────┐
       │    Text-to-Speech       │
       │        gTTS             │
       └────────────┬────────────┘
                    │
                    ▼
       ┌─────────────────────────┐
       │    Spoken Response      │
       │       🔊 Audio          │
       └─────────────────────────┘
```

*Note: The exact processing order and translation flow depend on the application's implementation.*

---

## 🔄 How It Works

1. 🎤 **Voice Input:** The user records audio through the Streamlit interface.
2. 📝 **Speech Transcription:** OpenAI Whisper converts the audio into text.
3. 🌍 **Language Processing:** Language detection and translation tools help process the transcribed input.
4. 🧠 **AI Response:** Ollama runs the configured language model to generate a response.
5. 🔊 **Speech Generation:** gTTS converts the generated response into audio.
6. 💬 **User Interaction:** The application presents the response through its interface and, where implemented, plays the generated speech.

---

## 📦 Prerequisites

Before running the application, ensure that you have:

- Python installed.
- pip package manager.
- FFmpeg installed and accessible to the application.
- Ollama installed.
- A compatible language model downloaded through Ollama.
- A working microphone for voice recording.
- An internet connection for services that require online access, such as Google Text-to-Speech or translation services.

---

## 🚀 Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2️⃣ Navigate to the Project Directory

```bash
cd Multilingual-AI-Voice-Assistant
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 4️⃣ Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Install and Configure Ollama

Install Ollama from its official website:

https://ollama.com/

Download the configured model:

```bash
ollama pull llama3.2
```

Start the model:

```bash
ollama run llama3.2
```

Ensure Ollama is running before using the application.

### 7️⃣ Configure FFmpeg

Install FFmpeg and ensure that its `bin` directory is available in your system's PATH.

Verify the installation:

```bash
ffmpeg -version
```

### 8️⃣ Run the Application

From the project directory, execute:

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the application.

---

## 📁 Project Structure

```text
Multilingual-AI-Voice-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
└── venv/
```

*The structure above is a basic example. Update it to match the actual files in your repository.*

---

## 📚 Python Dependencies

The application may require the following libraries, depending on the implementation:

- `streamlit`
- `openai-whisper`
- `ollama`
- `deep-translator`
- `langdetect`
- `gTTS`
- `audio-recorder-streamlit`
- `truststore`

Install the packages listed in your project's `requirements.txt`.

---

## 🔐 Privacy and Limitations

- 🎤 Audio is processed according to the configured speech-recognition workflow.
- 🦙 Ollama can run supported language models locally.
- 🌐 Translation and text-to-speech services may require internet access.
- 🔊 Recognition quality can vary depending on audio clarity, background noise, language, and accent.
- ⚙️ Performance depends on the selected Whisper model and available hardware.
- 🔒 Local language-model processing does not automatically mean that every part of the application operates offline.

---

## 🚀 Future Enhancements

Potential improvements include:

- 🔹 Add a wider range of supported languages.
- 🔹 Improve error handling for audio recording and transcription.
- 🔹 Add conversation history and contextual memory.
- 🔹 Integrate additional open-source language models.
- 🔹 Improve response speed and audio-processing performance.
- 🔹 Add configurable voice and language preferences.
- 🔹 Introduce a more advanced conversational interface.
- 🔹 Explore fully offline speech recognition and speech generation.
- 🔹 Deploy the application for broader access.

---

## 🎓 Learning Outcomes

This project explores:

- Speech recognition using OpenAI Whisper.
- Natural language processing and language detection.
- Multilingual translation workflows.
- Large language model integration using Ollama.
- Text-to-speech generation.
- Python application development.
- Streamlit-based user interface development.
- Integration of multiple AI technologies into one application.

---

## 👨‍💻 Author

**Suman Kumar Teja**

- 🐙 GitHub: [SumanKumar18](https://github.com/SumanKumar18)
- 💼 LinkedIn: [Connect with me](https://www.linkedin.com/in/sumank18)

---

## ⭐ Support

If you find this project interesting or useful, consider giving the repository a ⭐ on GitHub.

<p align="center">
  <b>Built with Python and AI 🚀</b><br>
  🎙️ Speech Recognition • 🌍 Multilingual AI • 🧠 Language Models
</p>
