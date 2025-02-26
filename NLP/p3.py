import speech_recognition as sr
import pyttsx3

def speak_text(text):
    """ Convert text to speech """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """ Recognize speech from microphone input """
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening... Speak something:")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)  # Capture audio

    try:
        # Convert speech to text using Google's Speech Recognition API
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        speak_text("You said " + text)  # Speak out the recognized text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        speak_text("Sorry, I could not understand that.")
    except sr.RequestError:
        print("Could not connect to the recognition service.")
        speak_text("I am having trouble connecting to the recognition service.")

# Run the speech recognition function
recognize_speech()
