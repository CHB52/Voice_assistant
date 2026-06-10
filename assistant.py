import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import sys
import time


def init_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)   # change index for different voice
    engine.setProperty("rate", 170)              # speaking speed
    engine.setProperty("volume", 1.0)
    return engine

engine = init_engine()
recognizer = sr.Recognizer()



def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Speech recognition service is unavailable. Check your internet connection.")
            return ""


def handle_command(command):
    if not command:
        return True

    # Greeting
    if any(word in command for word in ["hello", "hi", "hey"]):
        speak("Hello! How can I help you?")

    # Time
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}.")

    # Date
    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {today}.")

    # Day of week
    elif "day" in command:
        day = datetime.datetime.now().strftime("%A")
        speak(f"Today is {day}.")

    # Open websites
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://www.github.com")

    # Search Google
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching for {query}.")
            webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
        else:
            speak("What would you like me to search for?")

    # Joke
    elif "joke" in command:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer show up to work late? It had a hard drive.",
            "I told my computer I needed a break. Now it won't stop sending me vacation ads.",
        ]
        import random
        speak(random.choice(jokes))

    # Motivational quote
    elif "motivat" in command or "quote" in command:
        quotes = [
            "Believe you can and you're halfway there.",
            "The only way to do great work is to love what you do.",
            "Code is like humor. When you have to explain it, it's bad.",
        ]
        import random
        speak(random.choice(quotes))

    # How are you
    elif "how are you" in command:
        speak("I'm doing great, thanks for asking! Ready to help you.")

    # Name
    elif "your name" in command or "who are you" in command:
        speak("I'm your offline voice assistant, built with Python.")

    # Help
    elif "help" in command or "what can you do" in command:
        speak(
            "I can tell you the time, date, and day. "
            "I can open YouTube, Google, or GitHub. "
            "I can search Google, tell jokes, and share motivational quotes. "
            "Just ask!"
        )

    # Exit
    elif any(word in command for word in ["exit", "quit", "bye", "goodbye", "stop"]):
        speak("Goodbye! Have a great day.")
        return False

    else:
        speak("I'm not sure how to help with that. Try asking for the time, a joke, or say help.")

    return True


def main():
    speak("Voice assistant is ready. Say hello to get started, or say help to see what I can do.")
    running = True
    while running:
        command = listen()
        running = handle_command(command)
    sys.exit(0)

if __name__ == "__main__":
    main()
