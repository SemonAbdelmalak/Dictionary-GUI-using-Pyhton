import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.constants import GROOVE, LEFT
from PyDictionary import PyDictionary
import pyttsx3
from gtts import gTTS
import multiprocessing
from playsound import playsound
from translate import Translator

import sys

win = tk.Tk()
win.geometry("1000x400")


def Stop():
    p.terminate()
    os.remove("DIC.mp3")


class Speaking:

    def speak(self, audio):
        # Having the initial constructor of pyttsx3
        # and having the sapi5 in it as a parameter
        engine = pyttsx3.init('sapi5')

        # Calling the getter and setter of pyttsx3
        voices = engine.getProperty('voices')

        # Method for the speaking of the the assistant
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()


class GFG:
    def Dictionary(self):
        speak = Speaking()
        dic = PyDictionary()
        win.title("Welcoming")  # Label
        Lbl = tk.Label(win, text="Click for start", foreground='coral4', bg='aquamarine3', font=("Helvetica 40 bold"))
        Lbl.pack()  # Click event
        Lbl.place(x=300, y=150)

        # Adding Button

        def click():
            win2 = tk.Toplevel()
            win2.geometry("1200x600")
            win2.title("Dictionary")
            win2['bg'] = 'aquamarine3'

            def clicked():

                Meaning = dic.meaning(word.get())
                a = list(Meaning.keys())
                b = list(Meaning.values())
                global free
                free = ''
                for i in range(len(b)):
                    free += (word.get() + ' is a : ' + a[i] + '\n' + 'this word means : ' + '\n')
                    for j in range(len(b[i])):
                        free += (b[i][j] + '\n')

                meaning.configure(text=free, borderwidth=3, justify=LEFT, relief=GROOVE, anchor='w',
                                  font=("times", 15, "bold"),
                                  bg="lightblue")

            meaning = tk.Button(win2, text="Submit", font=("Helvetica 15 bold"), fg="coral4", command=clicked)
            meaning.pack()
            meaning.place(x=780, y=100)

            def voice():

                Meaning = dic.meaning(word.get())
                a = list(Meaning.keys())
                b = list(Meaning.values())
                global free1
                free1 = ''
                for i in range(len(b)):
                    free1 += (word.get() + ' is a : ' + a[i] + '\n' + 'this word means : ' + '\n')
                    for j in range(len(b[i])):
                        free1 += (b[i][j] + '\n')

                myobj = gTTS(text=str(free1), lang='en', slow=False)
                myobj.save("DIC.mp3")
                global p
                p = multiprocessing.Process(target=playsound, args=("DIC.mp3",))
                p.start()


            voiced = tk.Button(win2, text="Voicing", font=("Helvetica 15 bold"), fg="coral4", command=voice)
            voiced.pack()
            voiced.place(x=880, y=100)


            stop_btn = tk.Button(win2, text="Stop", font=("Helvetica 15 bold"), fg="coral4", command=Stop)
            stop_btn.place(x=845, y=150)


            action.configure(speak.speak("Which word do u want to find the meaning sir"))
            Lbl.configure(foreground='#CD3700')
            Lbl.configure(text="Welcome " + "\n" + "\n" + "to our dictionary", bg='aquamarine3',
                          font=("Helvetica 30 bold"))
            Lbl.place(x=300, y=100)

            # Frame 1
            frame = tk.Frame(win2)
            tk.Label(frame, text="Type a Word : ", font=("Helvetica 15 bold"), fg='coral4').pack(side=tk.LEFT)
            word = tk.Entry(frame, font=("Helvetica 15 bold"))
            word.pack()
            frame.pack(pady=10)
            frame.place(x=250, y=80)


# Frame 2
            frame1 = tk.Frame(win2)
            tk.Label(frame1, text="Meaning :- ", font=("Helvetica 20 bold"), fg='coral4').pack(side=tk.LEFT)
            meaning = tk.Label(frame1, text="", font=("Helvetica 15"))
            meaning.pack()
            frame1.pack(pady=10)
            frame1.place(x=50, y=200)
            photo2 = tk.PhotoImage(file=r"img2.png")
            photoimage2 = photo2.subsample(3,3)
            label2 = tk.Label(win2, image=photoimage2, bg="aquamarine3")
            label2.image = photo2
            label2.place(x=60, y=50)

            win2.mainloop()

        photo1 = tk.PhotoImage(file=r"img2.png")
        photoimage1 = photo1.subsample(2, 2)
        label1 = tk.Label(win, image=photoimage1, bg="aquamarine3")
        label1.image = photo1
        label1.place(x=700, y=50)

        photo3 = tk.PhotoImage(file=r"img1.png")
        photoimage3 = photo3.subsample(1, 1)
        label3 = tk.Label(win, image=photoimage3, bg="aquamarine3")
        label3.image = photo3
        label3.place(x=80, y=50)

        action = tk.Button(win, text="Start!", font=("Helvetica 20 bold"), width=10, height=1, command=click)
        action.pack()
        action.place(x=375, y=300)
        win["bg"] = "aquamarine3"
        win.mainloop()


if __name__ == '__main__':
    if sys.platform.startswith ( 'win' ):
        multiprocessing.freeze_support ()
    GFG()
    GFG.Dictionary(self=None)