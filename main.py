import os
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

# Specify the path to the FFmpeg executable
ffmpeg_path = "YOUR PATH TO: ffmpeg"

# Specify the path to the FFprobe executable
ffprobe_path = "YOUR PATH TO: fprobe"

# Load the audio file
audio_filename = "input.mp3"

# Export the audio as WAV format (required by the speech recognition library)
wav_filename = "input.wav"
os.system(f"{ffmpeg_path} -i {audio_filename} {wav_filename}")

# Convert speech to text
r = sr.Recognizer()
with sr.AudioFile(wav_filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data, language="ru-RU")  # Recognize Russian speech

# Translate the text to English
translator = Translator()
translated = translator.translate(text, src="ru", dest="vi")
translated_text = translated.text

# Convert the translated text to speech
tts = gTTS(text=translated_text, lang="vi")
output_filename = "output.mp3"
tts.save(output_filename)