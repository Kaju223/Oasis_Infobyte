import speech_recognition as sr

def listen():
    """Capture and recognize speech using the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for background noise... Please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        print("Listening...")

        try:
            # Listen with a timeout (5 seconds) and limit to 10 seconds for each phrase
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing your input...")

            # Recognize speech using Google API
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
        except sr.RequestError:
            print("Network error. Please check your internet connection.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None

# Example usage
while True:
    command = listen()
    if command:
        if "hello" in command:
            print("Hello! How can I assist you?")
        elif "time" in command:
            from datetime import datetime
            print("Current time:", datetime.now().strftime("%H:%M:%S"))
        elif "stop" in command:
            print("Goodbye!")
            break
        else:
            print("I'm sorry, I couldn't understand that.")
