import speech_recognition  as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while(1):     
    try:
        with sr.Microphone() as source2:
            # Adjust the recognizer sensitivity to ambient noise and record audio
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            
            # Using Google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            
            print(MyText)
            SpeakText(MyText)
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("unknown error occurred")