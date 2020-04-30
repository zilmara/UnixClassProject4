#!/usr/bin/python
#py matchingGUI.py
import os
import pygame
import pyglet
import tkinter
import tkinter.messagebox
import tkinter.font
from gtts import gTTS
#from tkinter import *

def helloCallBack():
	tkinter.messagebox.showinfo( "Hello Python", "Hello World")




top = tkinter.Tk()
language = 'en'

myText = "Hello Zilmara!"

helv60 = tkinter.font.Font(family='Helvetica', size=60, weight=tkinter.font.BOLD)

Button1 = tkinter.Button(top, text ="1", font=helv60, command = helloCallBack, 
						height=1, width=3)
Button2 = tkinter.Button(top, text ="2", font=helv60, command = helloCallBack, height=3, width=20)
Button3 = tkinter.Button(top, text ="3", font=helv60, command = helloCallBack, height=3, width=20)
Button4 = tkinter.Button(top, text ="4", font=helv60, command = helloCallBack, height=3, width=20)
Button5 = tkinter.Button(top, text ="5", font=helv60, command = helloCallBack, height=3, width=20)
Button6 = tkinter.Button(top, text ="6", font=helv60, command = helloCallBack, height=3, width=20)
Button7 = tkinter.Button(top, text ="7", font=helv60, command = helloCallBack, height=3, width=20)
Button8 = tkinter.Button(top, text ="8", font=helv60, command = helloCallBack, height=3, width=20)
Button9 = tkinter.Button(top, text ="9", font=helv60, command = helloCallBack, height=3, width=20)
Button10 = tkinter.Button(top, text ="10", font=helv60, command = helloCallBack, height=3, width=20)

top.rowconfigure((0, 2), weight=1 )
top.columnconfigure((0, 2), weight=1 )

Button1.grid(row=0, column=0, columnspan=1)
Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
Button5.pack()
Button6.pack()
Button7.pack()
Button8.pack()
Button9.pack()
Button10.pack()

myobj = gTTS(text=myText, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 

pygame.mixer.init()
pygame.mixer.music.load("welcome.mp3")
pygame.mixer.music.play()



#music = pyglet.media.load("welcome.mp3", streaming=False)
#music.play()

top.mainloop()