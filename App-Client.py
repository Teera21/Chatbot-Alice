import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import os
from markdown import markdown 
import speech_recognition as sr
import time
from gtts import gTTS
from playsound import playsound #ใช้สำหรับเล่นไฟล์เสียง
import requests
import json
from tkinter import PhotoImage,Button, Frame, Label


root = tk.Tk()
root.geometry("550x650")
root.title('Alice')
photo = PhotoImage(file = "logo3.png")
root.iconphoto(False, photo)


def open_url():
    print('hellow world')
####################
frame2 = Frame(root)
frame2.pack()
frame2.place(anchor='center', relx=0.5, rely=0.65)

text = Image.open('text.png')
text = text.resize((500, 500))
text = ImageTk.PhotoImage(text)
tx_label = Label(frame2, image = text)
tx_label.pack()

frame = Frame(root)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.3)

logo = Image.open('logo3.png')
logo = logo.resize((400, 400))
logo = ImageTk.PhotoImage(logo)
label = Label(frame, image = logo)
label.pack()

frame3 = Frame(root)
frame3.pack()
frame3.place(anchor='center', relx=0.5, rely=0.84)

button = Image.open('Button.png')
button = button.resize((100, 220))
button = ImageTk.PhotoImage(button)
button_lb = Label(frame3, image = button)
button_lb.pack(ipadx=50)
button_lb.bind("<Button-1>", lambda e:run())

def run():
    def speak(audioString):
        i=0
        print(audioString)
        tts = gTTS(text=audioString,lang = 'th')
        file1 = str("hello" + str(i) + ".mp3")
        tts.save(file1)
        playsound(file1,True)
        os.remove(file1)
        i = i+1    

    # record audio function
    def recordAudio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("เริ่มพูดกับ Alice ได้เลย!!")
            audio = r.listen(source)

        data = ""
        try:
            data = r.recognize_google(audio,language="th")
            print("คุณต้องการพูดว่า : " + data)
        except sr.UnknownValueError:
            print("ไม่มีคำที่คุณพูดในคลังการสื่อสารของ Alice ต้องขอ อภัยด้วยนะคะ")  
        return data

    def recordAudioEng():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
    
        data = ""
        try:
            data = r.recognize_google(audio,language="en")
            print("You said: " + data)
        except sr.UnknownValueError:
            print("ไม่มีคำที่คุณพูดในคลังการสื่อสารของ Alice ต้องขอ อภัยด้วยนะคะ")
        return data

    speak("หนูคือ alice หากมีอะไรที่สงสัย สามารถถาม Alice ได้เลยค่ะ")
    data = recordAudio()

    r = requests.post(url='http://6a28-34-73-104-156.ngrok.io/correctText',data=json.dumps({"text":data}))
    x = str(r.text)
    speak(x + 'ค่ะ')
    time.sleep(1)
        
root.mainloop()