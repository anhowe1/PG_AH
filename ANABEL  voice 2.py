import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch ("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak ("What video should we watch?")
    print ("Listening...")
    audio = r.listen(source)
    print ("thinking...")

try:
    words = r.recognize_google(audio)
    speak.Speak ("Ok, let's look for" + r.recognize_google(audio))
    wb.open ("https://www.youtube.com/results?search_query=" + words)

except sr. UnknownValueError:
    print ("Sorry I didn't understand")
except sr.RequestError as e:
    print ("Could not requests from Google Speach Recognition service;".format(e))


    
