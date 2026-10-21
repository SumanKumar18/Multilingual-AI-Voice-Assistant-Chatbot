from io import BytesIO
import os
import tempfile

import streamlit as st
import truststore
from faster_whisper import WhisperModel
import ollama
from gtts import gTTS

truststore.inject_into_ssl()

st.set_page_config(
    page_title="Multilingual Voice Chatbot",
    page_icon="🌍",
    layout="centered",
)
THEMES = {
    "Aurora": {"background": "radial-gradient(ellipse at 8% 4%, #f6dff2 0%, transparent 34%), radial-gradient(ellipse at 94% 12%, #dce8ff 0%, transparent 38%), linear-gradient(145deg, #faf7ff 0%, #f2f4ff 52%, #fff4ef 100%)", "surface": "rgba(255,255,255,.78)", "text": "#29243d", "muted": "#746d86", "border": "rgba(255,255,255,.9)", "accent_bg": "#f0e8ff", "accent": "#7652c8"},
    "Ocean": {"background": "linear-gradient(145deg, #f7f9ff 0%, #edf4ff 55%, #f8fbff 100%)", "surface": "#ffffff", "text": "#17233f", "muted": "#596780", "border": "#dfe8f5", "accent_bg": "#eaf0ff", "accent": "#3656a3"},
    "Light": {"background": "#f7f8fa", "surface": "#ffffff", "text": "#202733", "muted": "#657080", "border": "#e2e5e9", "accent_bg": "#edf2f7", "accent": "#35485f"},
    "Dark": {"background": "#111827", "surface": "#1f2937", "text": "#f3f6fc", "muted": "#bdc7d8", "border": "#374151", "accent_bg": "#293a58", "accent": "#bdd1ff"},
}

st.sidebar.markdown("### 🎨 Appearance")
theme_name = st.sidebar.selectbox("Choose a theme", list(THEMES), index=0)
colors = THEMES[theme_name]

st.markdown(f"""
<style>
.block-container {{max-width: 860px; padding-top: 2rem; padding-bottom: 5rem;}}
.stApp {{background: {colors['background']}; color: {colors['text']};}}
[data-testid="stHeader"] {{background: transparent;}}
.hero {{position: relative; overflow: hidden; padding: 2rem 2.1rem; border: 1px solid {colors['border']}; border-radius: 28px;
       background: {colors['surface']}; backdrop-filter: blur(18px);
       box-shadow: 0 18px 50px rgba(75, 58, 125, .10); margin-bottom: 1.5rem;}}
.hero::after {{content: ""; position: absolute; width: 190px; height: 190px; right: -42px; top: -64px;
               border-radius: 50%; background: radial-gradient(circle, rgba(205,174,255,.38), rgba(255,204,218,.08) 68%, transparent 72%);}}
.hero-tag {{display: inline-block; padding: .34rem .78rem; border-radius: 999px;
           background: {colors['accent_bg']}; color: {colors['accent']}; font-size: .76rem; font-weight: 700; letter-spacing: .08em;}}
.hero h1 {{position: relative; z-index: 1; margin: .85rem 0 .35rem; color: {colors['text']}; font-size: 2.35rem; letter-spacing: -.04em;}}
.hero p {{position: relative; z-index: 1; margin: 0; color: {colors['muted']}; font-size: 1rem;}}
[data-testid="stChatMessage"], [data-testid="stVerticalBlockBorderWrapper"] {{
  border: 1px solid {colors['border']}; border-radius: 22px; background: {colors['surface']};
  box-shadow: 0 8px 28px rgba(55, 48, 90, .06); backdrop-filter: blur(14px);
}}
[data-testid="stChatMessage"] {{padding: 1rem 1.15rem;}}
[data-testid="stSidebar"] {{background: {colors['surface']};}}
.stMarkdown, .stCaption {{color: {colors['text']};}}
div.stButton > button {{border-radius: 14px; border: 1px solid {colors['border']};}}
div.stButton > button:hover {{border-color: {colors['accent']}; color: {colors['accent']};}}
[data-testid="stAudioInput"] {{border-radius: 16px;}}
[data-testid="stChatInput"] {{border-radius: 18px;}}
</style>
<div class="hero">
  <span class="hero-tag">VOICE · CHAT · LISTEN</span>
  <h1>🌍 Voice Chat</h1>
  <p>Ask a question by voice or text. Read the answer or listen to it.</p>
</div>
""", unsafe_allow_html=True)

if "audio_widget_version" not in st.session_state:
    st.session_state.audio_widget_version = 0
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "ollama_history" not in st.session_state:
    st.session_state.ollama_history = []


@st.cache_resource(show_spinner="Loading speech recognition model...")
def load_model():
    # Whisper detects the spoken language automatically in transcribe_audio().
    return WhisperModel("small", device="cpu", compute_type="int8")


whisper_model = load_model()

LANGUAGE_NAMES = {
    "en": "English", "kn": "Kannada", "te": "Telugu", "ta": "Tamil",
    "ml": "Malayalam", "hi": "Hindi", "bn": "Bengali", "gu": "Gujarati",
    "mr": "Marathi", "pa": "Punjabi", "ur": "Urdu", "ar": "Arabic",
    "zh": "Chinese", "ja": "Japanese", "ko": "Korean", "fr": "French",
    "es": "Spanish", "de": "German", "it": "Italian", "pt": "Portuguese",
    "ru": "Russian", "nl": "Dutch", "tr": "Turkish", "id": "Indonesian",
    "vi": "Vietnamese", "th": "Thai", "fa": "Persian", "pl": "Polish",
    "uk": "Ukrainian", "sw": "Swahili", "he": "Hebrew", "el": "Greek",
    "sv": "Swedish", "da": "Danish", "fi": "Finnish", "no": "Norwegian",
    "cs": "Czech", "ro": "Romanian", "hu": "Hungarian",
}


def transcribe_audio(audio_file):
    """Read Streamlit's WAV recording and detect/transcribe its language with Whisper."""
    temp_path = None
    try:
        audio_file.seek(0)
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(audio_file.read())

        segments, info = whisper_model.transcribe(
            temp_path,
            language=None,
            task="transcribe",
            beam_size=5,
            condition_on_previous_text=False,
            vad_filter=False,
        )
        transcript = " ".join(segment.text.strip() for segment in segments).strip()
        return transcript, info.language or "en", float(info.language_probability or 0.0)
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)


def translate_with_ollama(text, source_language, target_language):
    source_name = LANGUAGE_NAMES.get(source_language, source_language)
    target_name = LANGUAGE_NAMES.get(target_language, target_language)
    result = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    f"Translate the text from {source_name} to {target_name}. "
                    "Return only the translation. Do not answer or explain."
                ),
            },
            {"role": "user", "content": text},
        ],
    )
    return result["message"]["content"].strip()


def answer_in_english(messages):
    result = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant. The conversation is in English. "
                    "Answer accurately and clearly in English. Keep replies concise unless detail is needed."
                ),
            },
            *messages,
        ],
    )
    return result["message"]["content"].strip()


def make_speech(text, language):
    audio = BytesIO()
    gTTS(text=text, lang=language).write_to_fp(audio)
    return audio.getvalue()


with st.sidebar:
    st.markdown("### 💬 Your chat")
    st.caption(f"{len(st.session_state.chat_history)} messages so far")
    if st.button("＋ New conversation", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.ollama_history = []
        st.session_state.audio_widget_version += 1
        st.rerun()
    st.divider()
    st.markdown("**How to use**")
    st.caption("🎙️ Record a message in the language you speak.")
    st.caption("⌨️ Or type a message in English.")
    st.caption("🔊 Listen to the reply with the audio player.")

# Conversation area
if not st.session_state.chat_history:
    with st.container(border=True):
        st.markdown("### 👋 Welcome")
        st.write("Your conversation will appear here. Start with a voice recording or type a message below.")

for turn in st.session_state.chat_history:
    with st.chat_message("user", avatar="🧑"):
        st.write(turn["user_text"])
        if turn["language"] != "en":
            st.caption(
                f"Detected: {LANGUAGE_NAMES.get(turn['language'], turn['language'].upper())} "
                f"({turn['language']}) · {round(turn['confidence'] * 100)}% confidence"
            )
    with st.chat_message("assistant", avatar="🌍"):
        st.markdown("**English**")
        st.write(turn["english_answer"])
        if turn["language"] != "en":
            language_name = LANGUAGE_NAMES.get(turn["language"], turn["language"].upper())
            with st.expander(f"See the {language_name} reply"):
                st.write(turn["translated_answer"])
        if turn.get("audio"):
            st.audio(turn["audio"], format="audio/mp3")
        if turn.get("voice_error"):
            st.caption(turn["voice_error"])

with st.container(border=True):
    st.markdown("**🎙️ Send a voice message**")
    st.caption("Record a short question. The app will add it to this conversation.")
    audio_key = f"voice_input_{st.session_state.audio_widget_version}"
    audio_file = st.audio_input(
        "Record voice",
        sample_rate=16000,
        key=audio_key,
        label_visibility="collapsed",
    )
typed_text = st.chat_input("Or type a message in English...")

if typed_text or audio_file is not None:
    new_turn = None
    try:
        if typed_text:
            user_text = typed_text.strip()
            language = "en"
            confidence = 1.0
            english_question = user_text
        else:
            with st.spinner("Detecting language and transcribing..."):
                user_text, language, confidence = transcribe_audio(audio_file)
            if not user_text:
                st.error("I couldn't recognize speech. Please record a clear, complete sentence and try again.")
                st.session_state.audio_widget_version += 1
                st.rerun()
            with st.spinner("Understanding your message..."):
                english_question = (
                    user_text if language == "en"
                    else translate_with_ollama(user_text, language, "en")
                )

        messages_for_reply = [
            *st.session_state.ollama_history,
            {"role": "user", "content": english_question},
        ]
        with st.spinner("Thinking..."):
            english_answer = answer_in_english(messages_for_reply)

        translated_answer = (
            english_answer if language == "en"
            else translate_with_ollama(english_answer, "en", language)
        )
        new_turn = {
            "user_text": user_text,
            "language": language,
            "confidence": confidence,
            "english_answer": english_answer,
            "translated_answer": translated_answer,
        }

        # Keep the ongoing chat context in English so every language shares one conversation.
        st.session_state.ollama_history.extend([
            {"role": "user", "content": english_question},
            {"role": "assistant", "content": english_answer},
        ])
        try:
            with st.spinner("Creating voice reply..."):
                new_turn["audio"] = make_speech(translated_answer, language)
        except Exception as exc:
            new_turn["voice_error"] = f"Voice output unavailable: {type(exc).__name__}: {exc}"
        st.session_state.chat_history.append(new_turn)
    except Exception as exc:
        st.error(f"Couldn't process that message: {type(exc).__name__}: {exc}")
    finally:
        st.session_state.audio_widget_version += 1
    st.rerun()
