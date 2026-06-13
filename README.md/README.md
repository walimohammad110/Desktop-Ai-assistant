# Jarvis AI Assistant (Python)

A voice-controlled AI assistant built with Python, inspired by Jarvis from Iron Man.
This assistant can listen to voice commands, respond with speech, open websites, play music, and send WhatsApp messages.

## Features

* Voice command recognition
* Text-to-speech responses
* GUI built using Tkinter
* Play music on YouTube
* Tell current time
* Send WhatsApp messages instantly
* Simple chatbot interactions

## Project Structure


Jarvis/
│
├── main.py
├── action.py
├── ugui.py
├── speech_to_text.py
├── text_speach.py
├── whatsapp.py
├── requirements.txt
└── README.md
```

## Technologies Used

* Python 3
* Tkinter
* SpeechRecognition
* pyttsx3
* PyWhatKit
* Pillow

## Installation

### 1. Clone repository

```bash
git clone YOUR_GITHUB_REPO_LINK
cd Jarvis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Required Packages

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install pywhatkit
pip install pillow
pip install sounddevice
pip install PILLOW
pip install tkinter

```

## Run Project

```bash
python ugui.py
```

## Supported Commands

Example commands:

* “Hello”
* “What is your name”
* “Play music”
* “Send message”
* “time”
* “Shutdown”

## How WhatsApp Messaging Works

Jarvis can send WhatsApp messages using WhatsApp Web.

Steps:

1. Say **send message**
2. Speak contact name
3. Speak message
4. Jarvis sends message automatically

Make sure:

* You are logged into WhatsApp Web
* Internet connection is active

## Future Improvements

* Weather updates
* AI chat integration
* App launching
* Face recognition
* Automation tasks

## Author

Developed by **Wali Mohammad**
