import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch ("SAPI.SpVoice")
speak.Speak ("what's your favorite color?")

answer = pg.prompt ("Enter your favorite color below.")

if answer == "purple"
    speak.Speak ("Wow, I love purple flowers")
elif answer == "blue"
    speak.Speak(" I love the color blue")
else:
    speak.Speak ("wow, thats great! I love" + answer)


speak.Speak ("What video would you like to watch?")
video = pg.prompt ("Enter your video below")
speak.Speak ("Ok, let's look for " + video + "on youtube")

wb.open ("https://www.youtube.com/results?search_query=" + video)
