<div align="center">

# 🌍 Multilingual AI Voice Assistant

### 🎙️ Breaking Language Barriers with Artificial Intelligence

An AI-powered voice assistant integrating speech recognition, Generative AI, multilingual translation, and text-to-speech to enable interactive voice-based communication.

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Whisper](https://img.shields.io/badge/Whisper-Speech%20Recognition-412991?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge&logo=ollama&logoColor=white)
![Generative AI](https://img.shields.io/badge/Generative-AI-8A2BE2?style=for-the-badge)

</div>

---

## 📌 Overview

The **Multilingual AI Voice Assistant** is a Python-based application designed to make AI interaction more accessible through voice communication.

The application converts spoken input into text using OpenAI Whisper, generates AI-powered responses using Llama 3.2 through Ollama, translates responses into the user's language, and converts the final text into speech using Google Text-to-Speech (gTTS).

Built with Streamlit, this project demonstrates the integration of speech recognition, Large Language Models (LLMs), Natural Language Processing (NLP), translation, and speech synthesis into a unified application.

---

## ✨ Key Features

- 🎙️ **Speech Recognition:** Converts spoken input into text using OpenAI Whisper.
- 🤖 **AI-Powered Responses:** Generates conversational responses using Llama 3.2 through Ollama.
- 🌐 **Language Detection:** Identifies the language of recognized text.
- 🔄 **Multilingual Translation:** Translates AI-generated responses into the detected language.
- 🔊 **Text-to-Speech:** Converts text responses into spoken audio using gTTS.
- 💻 **Interactive Interface:** Provides a browser-based interface built with Streamlit.
- 🧩 **AI Integration:** Combines multiple AI and language-processing components in one application.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🎨 Streamlit | Web application interface |
| 🎙️ OpenAI Whisper | Speech-to-text transcription |
| 🧠 Ollama | Local LLM runtime |
| 🤖 Llama 3.2 | AI response generation |
| 🌐 deep-translator | Text translation |
| 🔎 langdetect | Language identification |
| 🔊 gTTS | Text-to-speech generation |
| 🎧 audio-recorder-streamlit | Browser-based audio recording |
| 🎵 FFmpeg | Audio processing for Whisper |

---

## 🏗️ System Architecture

```text
                   🎙️ User Voice Input
                           │
                           ▼
                   🎧 Audio Recording
                           │
                           ▼
                   🗣️ OpenAI Whisper
                    Speech-to-Text
                           │
                           ▼
                    🌐 Language Detection
                           │
                           ▼
                   🤖 Ollama + Llama 3.2
                    AI Response Generation
                           │
                           ▼
                    🔄 Response Translation
                           │
                           ▼
                       🔊 gTTS
                     Speech Synthesis
                           │
                           ▼
                   💬 Spoken AI Response
```

---

## 🌍 Supported Languages

The application is configured for the following languages:

| Language | Code |
|---|---|
| 🇬🇧 English | `en` |
| 🇮🇳 Tamil | `ta` |
| 🇮🇳 Hindi | `hi` |
| 🇮🇳 Telugu | `te` |
| 🇮🇳 Malayalam | `ml` |
| 🇮🇳 Kannada | `kn` |
| 🇮🇳 Bengali | `bn` |
| 🇫🇷 French | `fr` |
| 🇪🇸 Spanish | `es` |
| 🇩🇪 German | `de` |

*Language availability depends on the application's implementation and the capabilities of the speech recognition, translation, and text-to-speech services.*

---

## 📂 Project Structure

```text
Multilingual-AI-Voice-Assistant/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Files excluded from Git
│
└── screenshots/             # Optional application screenshots
    └── app-preview.png
```

---

## ⚙️ Installation and Setup

### 📋 Prerequisites

Install the following tools before running the application:

- Python
- Git
- FFmpeg
- Ollama
- A compatible Llama 3.2 model

### 1️⃣ Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/Multilingual-AI-Voice-Assistant.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd Multilingual-AI-Voice-Assistant
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### 4️⃣ Activate the Virtual Environment

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**

```cmd
.venv\Scripts\activate.bat
```

### 5️⃣ Install Python Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6️⃣ Install FFmpeg

Download FFmpeg:

https://ffmpeg.org/download.html

Configure FFmpeg in your system's `PATH`.

Verify the installation:

```bash
ffmpeg -version
```

### 7️⃣ Configure Ollama

Download Ollama:

https://ollama.com/download

Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Ensure Ollama is running before using the application.

### 8️⃣ Launch the Application 🚀

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal. The default address is:

http://localhost:8501

> 💡 **Note:** Whisper may download its model during the first run. Initial startup and transcription can take some time.

---

## 📦 Dependencies

The project's Python dependencies are listed in `requirements.txt`.

Create this file in the project root and add:

```text
streamlit
openai-whisper
ollama
deep-translator
langdetect
gTTS
audio-recorder-streamlit
truststore
```

Install them using:

```bash
pip install -r requirements.txt
```

**Additional requirements:**

- **FFmpeg:** Required for Whisper audio processing.
- **Ollama:** Runs the local language model.
- **Llama 3.2:** The model used for generating AI responses.

> ⚠️ Dependency compatibility can vary by Python version and operating system. Use a compatible Python environment if installation fails.

---

## 🛡️ Git Configuration

### `.gitignore`

Create a file named `.gitignore` in the project root.

Add the following:

```gitignore
# Python cache
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
.venv/
venv/
env/

# Environment variables and secrets
.env
.env.*

# IDE configuration
.vscode/

# Generated audio files
*.mp3
*.wav
*.m4a

# Model caches
.cache/

# Operating system files
.DS_Store
Thumbs.db
```

This prevents common temporary files, virtual environments, local recordings, and environment configuration files from being included in Git commits.

**Important:** Never upload passwords, API keys, private recordings, or other sensitive information.

---

## 🚀 Upload the Project to GitHub

After creating your repository on GitHub, open a terminal inside the project folder.

### 1️⃣ Initialize Git

```bash
git init
```

### 2️⃣ Stage the Project Files

```bash
git add app.py README.md requirements.txt .gitignore
```

### 3️⃣ Create the Initial Commit

```bash
git commit -m "Initial commit: Multilingual AI Voice Assistant"
```

### 4️⃣ Set the Main Branch

```bash
git branch -M main
```

### 5️⃣ Connect the Remote Repository

Replace the example URL with your actual GitHub repository URL.

```bash
git remote add origin https://github.com/YOUR_USERNAME/Multilingual-AI-Voice-Assistant.git
```

### 6️⃣ Push to GitHub

```bash
git push -u origin main
```

If Git reports that `origin` already exists, check the configured remote using:

```bash
git remote -v
```

Do not add a duplicate remote.

---

## 🧠 Concepts Demonstrated

This project explores practical applications of:

- 🎙️ Automatic Speech Recognition (ASR)
- 🧠 Large Language Models (LLMs)
- ✍️ Natural Language Processing (NLP)
- 🌐 Multilingual text processing
- 🔄 AI model integration
- 🔊 Speech synthesis
- 🖥️ Interactive web application development
- ⚙️ Python dependency management
- 💻 Local AI model deployment

---

## 🔮 Future Enhancements

- 💬 Conversation history and contextual memory
- ⚡ Improved transcription and response speed
- 🎤 Enhanced real-time voice interaction
- 🌍 Expanded language support
- 🎨 Improved interface and accessibility
- 📱 Mobile-friendly user experience
- 📄 Conversation export functionality
- 🧠 Additional LLM integrations

---

## 🎯 Project Objective

The objective of this project is to explore the integration of speech recognition, Generative AI, translation, and speech synthesis to develop an accessible multilingual conversational application.

It provides practical experience in combining AI models, language-processing tools, and web technologies into a unified Python application.

---

## 👨‍💻 Author

<div align="center">

### Suman Kumar Teja

💻 **GitHub:** [@SumanKumar18](https://github.com/SumanKumar18)

🔗 **LinkedIn:** [Connect with me](https://www.linkedin.com/in/sumank18)

</div>

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

Feedback, suggestions, and constructive contributions are welcome!

---

<div align="center">

### 🌍 Connecting People and AI Through Voice

**Built with Python, Speech AI, and Generative AI.** 🚀

</div>
