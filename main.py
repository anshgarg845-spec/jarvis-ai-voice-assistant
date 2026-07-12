import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(command):
    print("Command:", command)

    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open twitter" in command:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    else:
        speak("Sorry, I don't know that command yet.")


if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:

                print("\nWaiting for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=1)

                audio = recognizer.listen(
                    source,
                    timeout=10,
                    phrase_time_limit=5
                )

            word = recognizer.recognize_google(audio)

            print("You said:", word)

            if "jarvis" in word.lower():

                speak("Yes Sir")

                with sr.Microphone() as source:

                    print("Listening for command...")

                    recognizer.adjust_for_ambient_noise(source, duration=0.5)

                    audio = recognizer.listen(
                        source,
                        timeout=10,
                        phrase_time_limit=7
                    )

                command = recognizer.recognize_google(audio)

                processCommand(command)

        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")

        except sr.RequestError:
            print("Internet connection problem.")

        except Exception as e:
            print("Error:", e)