# create a program for text to speech 
import pyttsx3

# Initialize the engine

engine = pyttsx3.init()

# Set the voice

engine.setProperty('voice', 'en-US')

# Set the rate

engine.setProperty('rate', 150)

# Set the volume



# Convert text to speech

text = "Hello, welcome to AI Training"

engine.say(text)

# Run and wait for the audio to finish

engine.runAndWait()
