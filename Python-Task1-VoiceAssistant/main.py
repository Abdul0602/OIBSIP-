import datetime
import webbrowser

import pyttsx3
import speech_recognition as sr


def speak(text):
    """Speak a response and also show it in the terminal."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """Capture and recognize one spoken command."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

        command = recognizer.recognize_google(audio)
        command = command.lower().strip()
        print(f"You: {command}")
        return command

    except sr.WaitTimeoutError:
        speak("I did not hear anything. Please try again.")
    except sr.UnknownValueError:
        speak("Sorry, I could not understand you. Please repeat.")
    except sr.RequestError:
        speak("The speech recognition service is unavailable right now.")
    except OSError:
        speak("I could not access the microphone. Please check your microphone settings.")

    return ""


def tell_date():
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    speak(f"Today is {today}.")


def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")


def search_web(command):
    """Open a browser search for text following the word 'search'."""
    query = command.replace("search", "", 1).strip()

    if not query:
        speak("Please tell me what you want me to search for.")
        return

    speak(f"Searching the web for {query}.")
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(url)


def handle_command(command):
    """Handle the beginner-level voice assistant commands."""
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        tell_time()

    elif "date" in command or "today" in command:
        tell_date()

    elif command.startswith("search"):
        search_web(command)

    elif command in {"exit", "quit", "stop", "goodbye"}:
        speak("Goodbye!")
        return False

    elif command:
        speak("I do not know that command yet. Try hello, time, date, search, or exit.")

    return True


engine = pyttsx3.init()
recognizer = sr.Recognizer()


def main():
    speak("Voice assistant started. Say hello, ask for the time or date, search for a topic, or say exit.")

    running = True
    while running:
        command = listen()
        if command:
            running = handle_command(command)


if __name__ == "__main__":
    main()
