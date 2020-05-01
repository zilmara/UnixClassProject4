#!/usr/bin/python
#py matchingGUI.py
import os
import pygame
import pyglet
import tkinter
import tkinter.messagebox
import tkinter.font
import tkinter.ttk
from tkinter.ttk import Frame, Button, Style
from random import randrange
from gtts import gTTS

def helloCallBack():
    tkinter.messagebox.showinfo( "Hello Python", "Hello World")

def SoundNumbers():
        
    #button1.pack()
    language = 'en'
    print(randrange(1,11))
    myText = "Hello Zilmara!"

    helv60 = tkinter.font.Font(family='Helvetica', size=10, weight=tkinter.font.BOLD)

    myobj = gTTS(text=myText, lang=language, slow=False) 
      
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("welcome1.mp3") 

    pygame.mixer.init()
    pygame.mixer.music.load("welcome.mp3")
    pygame.mixer.music.play()


def main():

    root = tkinter.Tk()
    # Add Label to the root window 
    tkinter.Label(root, text = 'Learning Numbers', font =('Verdana', 15)).pack(pady = 10) 
	
    #Set up photo images for GUI
    photo1 = tkinter.PhotoImage(file = "red1.png") 
    photo2 = tkinter.PhotoImage(file = "blue2.png") 
    photo3 = tkinter.PhotoImage(file = "black3.png") 
    photo4 = tkinter.PhotoImage(file = "purple4.png") 
    photo5 = tkinter.PhotoImage(file = "red5.png") 
    photo6 = tkinter.PhotoImage(file = "purple6.png")
    photo7 = tkinter.PhotoImage(file = "teal7.png") 
    photo8 = tkinter.PhotoImage(file = "gray8.png") 
    photo9 = tkinter.PhotoImage(file = "red9.png") 
    photo10 = tkinter.PhotoImage(file = "gold10.png") 
    startPhoto = tkinter.PhotoImage(file = "start.png")
    
    # Resizing image to fit on button 
    photo1 = photo1.zoom(2) 
    photo1 = photo1.subsample(10,10) 
    photo2 = photo2.zoom(3) 
    photo2 = photo2.subsample(11,11) 
    photo3 = photo3.zoom(3) 
    photo3 = photo3.subsample(11, 11)
    photo4 = photo4.zoom(3)	
    photo4 = photo4.subsample(11, 11) 
    photo5 = photo5.zoom(3)
    photo5 = photo5.subsample(11, 11) 
    photo6 = photo6.zoom(3)
    photo6 = photo6.subsample(11, 11)
    photo7 = photo7.zoom(8)	
    photo7 = photo7.subsample(11, 11)
    photo8 = photo8.zoom(8)	
    photo8 = photo8.subsample(11, 11)
    photo9 = photo9.zoom(3)	
    photo9 = photo9.subsample(11, 11)
    photo10 = photo10.zoom(10)	
    photo10 = photo10.subsample(11, 11)
    startPhoto = startPhoto.zoom(2)
    startPhoto = startPhoto.subsample(11, 11)

    #Set image on button
    tkinter.Button(root, text = 'Click Me !', command=SoundNumbers, image = photo1).place(x=50, y=150)
    tkinter.Button(root, text = 'Click Me !', image = photo2).place(x=200, y=100)
    tkinter.Button(root, text = 'Click Me !', image = photo3).place(x=400, y=50)
    tkinter.Button(root, text = 'Click Me !', image = photo4).place(x=600, y=100)
    tkinter.Button(root, text = 'Click Me !', image = photo5).place(x=800, y=150)
    tkinter.Button(root, text = 'Click Me !', image = photo6).place(x=30, y=400)
    tkinter.Button(root, text = 'Click Me !', image = photo7).place(x=220, y=450)
    tkinter.Button(root, text = 'Click Me !', image = photo8).place(x=400, y=500)
    tkinter.Button(root, text = 'Click Me !', image = photo9).place(x=580, y=450)
    tkinter.Button(root, text = 'Click Me !', image = photo10).place(x=780, y=400)
    
	#Start button
    tkinter.Button(root, text = 'Let\'s Begin!', image = startPhoto).place(x=440, y=330)
	
    root.wm_title("Matching Numbers")
    root.geometry("1000x750")
    root.mainloop()


if __name__== '__main__':
    main()