import pyttsx3
import sys
from customtkinter import *

words = ""

def speak():
    words = say.get()

    engine = pyttsx3.init()

    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    engine.say(words)
    engine.runAndWait()
        

window = CTk()
window.title("What to speak?")
window.geometry("500x120")

CTkLabel(window, text="What to say?").place(x=100, y=10)
say = CTkEntry(window, width=300)
say.place(x=100, y=35)

CTkButton(window, text="Speak", command=speak).place(x=100, y=70)
 
window.mainloop()

