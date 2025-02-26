import pyttsx3 
import speech_recognition as sr

# Initialize the engine

engine = pyttsx3.init()

# Set the voice

engine.setProperty('voice', 'en-US')

# Set the rate

engine.setProperty('rate', 150)

# Set the volume

