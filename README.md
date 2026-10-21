# 🌍 Multilingual AI Voice Assistant

A Python-based multilingual voice assistant integrating speech
recognition, AI-generated responses, translation, and voice output.

## Features

- Speech-to-text using OpenAI Whisper
- AI responses using Ollama and Llama 3.2
- Language detection
- Text translation
- Text-to-speech using gTTS
- Interactive Streamlit interface

## Technologies

- Python
- Streamlit
- OpenAI Whisper
- Ollama
- Llama 3.2
- deep-translator
- langdetect
- gTTS

## Installation

### 1. Clone the repository

git clone YOUR_REPOSITORY_URL

### 2. Enter the project folder

cd Multilingual-AI-Voice-Assistant

### 3. Create a virtual environment

python -m venv .venv

### 4. Activate the environment (Windows)

.venv\Scripts\activate

### 5. Install dependencies

python -m pip install -r requirements.txt

### 6. Install external requirements

Install FFmpeg and Ollama separately.

Download the language model:

ollama pull llama3.2

### 7. Run the application

python -m streamlit run app.py
