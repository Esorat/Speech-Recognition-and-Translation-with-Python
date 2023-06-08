**Speech Recognition and Translation with Python**

This repository contains a Python script that demonstrates how to perform speech recognition and translation using the SpeechRecognition, googletrans, and gTTS libraries. The script utilizes FFmpeg and FFprobe for audio file manipulation.

**Features:**

- Load an audio file in MP3 format.
- Convert the audio file to WAV format using FFmpeg.
- Recognize speech from the audio using the Google Speech Recognition API.
- Translate the recognized text to a desired language using the Google Translate API.
- Convert the translated text to speech using gTTS.
- Save the translated speech as an output audio file in MP3 format.

**Installation:**

1. Install FFmpeg and FFprobe:
   - Ensure you have Homebrew installed on your system. If not, install Homebrew by following the instructions at https://brew.sh/.
   - Open a terminal and run the following commands:
     ```
     brew install ffmpeg
     brew install fprobe
     ```

2. Install the required Python packages:
   - Open a terminal and run the following command:
     ```
     pip install speechrecognition googletrans gtts
     ```


**Usage:**

1. Specify the paths to FFmpeg and FFprobe executables in the script.
2. Provide the input audio file in MP3 format (named "input.mp3") in the same directory as the script.
3. Run the script.
4. The script will convert the input audio file to WAV format, recognize the speech using the Google Speech Recognition API, translate the text to a desired language using the Google Translate API, convert the translated text to speech using gTTS, and save the output audio file as "output.mp3".

Feel free to customize the code according to your specific requirements.

Enjoy exploring speech recognition and translation with Python!
