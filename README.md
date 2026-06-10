# 🎙️ Voice Assistant

A simple offline voice assistant built with Python. No API keys or internet required — just speak and it responds!

---

## Features

| Command | Example |
|---|---|
| Greeting | *"Hello"* / *"Hi"* |
| Current time | *"What's the time?"* |
| Current date | *"What's today's date?"* |
| Day of week | *"What day is it?"* |
| Open YouTube | *"Open YouTube"* |
| Open Google | *"Open Google"* |
| Open GitHub | *"Open GitHub"* |
| Google search | *"Search Python tutorials"* |
| Tell a joke | *"Tell me a joke"* |
| Motivation | *"Give me a motivational quote"* |
| Help | *"What can you do?"* |
| Exit | *"Goodbye"* / *"Exit"* |

---

## Tech Stack

- **Python 3.8+**
- [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/) — converts microphone input to text (uses Google's free speech API)
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) — offline text-to-speech engine
- [`PyAudio`](https://pypi.org/project/PyAudio/) — microphone access

> Speech recognition requires a one-time internet connection per query (Google's free STT service). All other features including text-to-speech work fully offline.

---

## Setup (Windows)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install PyAudio (Windows requires this step first)
```bash
pip install pipwin
pipwin install pyaudio
```

### 4. Install remaining dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the assistant
```bash
python assistant.py
```

---

## Troubleshooting

**Microphone not detected**
- Make sure your microphone is plugged in and set as the default input device in Windows Sound Settings.

**PyAudio install fails**
- Use `pipwin install pyaudio` instead of `pip install pyaudio`. If that also fails, download the `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install with `pip install <filename>.whl`.

**"Speech recognition service unavailable"**
- The speech-to-text step needs an internet connection. Check your Wi-Fi.

---

## Project Structure

```
voice-assistant/
├── assistant.py       # Main script
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

---

## License

MIT License — free to use and modify.
