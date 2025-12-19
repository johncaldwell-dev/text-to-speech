import pyttsx3
import sys
from customtkinter import *

words = ""
voiceid = 0

def speak(rate_number, volume_number):
    words = say.get()
    selected_voice = cbovoice.get()
    
    voiceid = voice_selection(selected_voice)
    
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[voiceid].id)
    engine.setProperty('rate', rate_number)
    engine.setProperty('volume', volume_number)

    engine.say(words)
    engine.runAndWait()

    clear_inputbox()


def clear_inputbox():
    say.delete(0, END)

def voice_selection(choice):
    
    if choice.lower() == "male":
        return 0
    elif choice.lower() == "female":
       return 1
    else:
        return 0
        

window = CTk()
window.title("What to speak?")
window.geometry("500x150")

CTkLabel(window, text="What to say?").place(x=100, y=10)
say = CTkEntry(window, width=300)
say.place(x=100, y=35)

voice = ["Male", "Female"]
cbovoice = CTkComboBox(window, values=voice)
cbovoice.place(x=250, y=70)
cbovoice.set("Male")


CTkButton(window, text="Speak", command=lambda:speak(rate_number=150, volume_number=1.0)).place(x=100, y=70)




 
window.mainloop()

