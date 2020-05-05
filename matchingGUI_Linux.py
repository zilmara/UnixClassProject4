#!/usr/bin/python

import os
import pygame
import pyglet
import random
import tkinter
import tkinter.messagebox
import tkinter.font
import tkinter.ttk
from tkinter.ttk import Frame, Button, Style
from random import randrange
from gtts import gTTS

count = 0
randomNumber = 0

def doneCallBack():
    tkinter.messagebox.showinfo( "Matching Game", "GOOD JOB!!!")
    exit()

def pressedOne():
    randomNumbers(1)

def pressedTwo():
    randomNumbers(2)

def pressedThree():
    randomNumbers(3)
	
def pressedFour():
    randomNumbers(4)

def pressedFive():
    randomNumbers(5)

def pressedSix():
    randomNumbers(6)	

def pressedSeven():
    randomNumbers(7)
	
def pressedEight():
    randomNumbers(8)
	
def pressedNine():
    randomNumbers(9)
	
def pressedTen():
    randomNumbers(10)	
	
def checkCorrectness(numberPressed, randomNumber):
    
    language = 'en-za'
    
    if (numberPressed == randomNumber):
        myText = "Correct!"
        global count
        count = count + 1
    else:
        myText = "Incorrect!"
		
    myobj = gTTS(text=myText, lang=language, slow=False) 
      
    myobj.save(myText + ".ogg") 

    pygame.mixer.init()
    pygame.mixer.music.load(myText + ".ogg")
    pygame.mixer.music.play()

def wordNum(randomNumber):
    if (randomNumber == 1):
        myText = "one"
    elif (randomNumber == 2):
        myText = "two"
    elif (randomNumber == 3):
        myText = "three"
    elif (randomNumber == 4):
        myText = "four"
    elif (randomNumber == 5):
        myText = "five"
    elif (randomNumber == 6):
        myText = "six"
    elif (randomNumber == 7):
        myText = "seven"
    elif (randomNumber == 8):
        myText = "eight"
    elif (randomNumber == 9):
        myText = "nine"
    elif (randomNumber == 10):
        myText = "ten"	
		
    return myText
	
def startNumbers():

    language = 'en-za'
	#Start with first random number
    global randomNumber
    randomNumber = randrange(1,11)
	
    myText = wordNum(randomNumber)
		
    myobj = gTTS(text=myText, lang=language, slow=False) 
      
    # Saving the converted audio in a mp3 file named 
    myobj.save(myText + ".ogg") 
    #read first random number
    pygame.mixer.init()
    pygame.mixer.music.load(myText+ ".ogg")
    pygame.mixer.music.play()	
	
def randomNumbers(numberPressed):
    
    global randomNumber
    checkCorrectness(numberPressed, randomNumber)

    language = 'en-za'
    randomNumber = randrange(1,11)
    if (randomNumber == 1):
        myText = "one"
    elif (randomNumber == 2):
        myText = "two"
    elif (randomNumber == 3):
        myText = "three"
    elif (randomNumber == 4):
        myText = "four"
    elif (randomNumber == 5):
        myText = "five"
    elif (randomNumber == 6):
        myText = "six"
    elif (randomNumber == 7):
        myText = "seven"
    elif (randomNumber == 8):
        myText = "eight"
    elif (randomNumber == 9):
        myText = "nine"
    elif (randomNumber == 10):
        myText = "ten"
	
    if (count == 20):
        doneCallBack()
    else:
        myobj = gTTS(text=myText, lang=language, slow=False) 
        filename = myText + ".ogg"

        myobj.save(filename) 
	
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

def main():

    root = tkinter.Tk()
    root.config(cursor=('circle'))
    # Add Label to the root window 
    tkinter.Label(root, text = 'Learning Numbers', font =('Verdana', 15)).pack(pady = 10) 
	
    #Set up photo images for GUI
    #photo1 = tkinter.PhotoImage(file = "red1.png") 
    photo1 = tkinter.PhotoImage(file = "1092116.png")
    photo2 = tkinter.PhotoImage(file = "blue2.png") 
    #photo3 = tkinter.PhotoImage(file = "black3.png") 
    photo3 = tkinter.PhotoImage(file = "2041976.png")
    photo4 = tkinter.PhotoImage(file = "purple4.png") 
    #photo5 = tkinter.PhotoImage(file = "red5.png") 
    photo5 = tkinter.PhotoImage(file = "1803800.png")
    photo6 = tkinter.PhotoImage(file = "purple6.png")
    #photo7 = tkinter.PhotoImage(file = "teal7.png") 
    photo7 = tkinter.PhotoImage(file = "675119.png")
    photo8 = tkinter.PhotoImage(file = "gray8.png") 
    #photo9 = tkinter.PhotoImage(file = "red9.png") 
    photo9 = tkinter.PhotoImage(file = "numNine.png")
    photo10 = tkinter.PhotoImage(file = "gold10.png") 
    startPhoto = tkinter.PhotoImage(file = "start.png")
    
    # Resizing image to fit on button 
    photo1 = photo1.zoom(1) 
    photo1 = photo1.subsample(8,8) 
    photo2 = photo2.zoom(3) 
    photo2 = photo2.subsample(11,11) 
    photo3 = photo3.zoom(1) 
    photo3 = photo3.subsample(8, 8)
    photo4 = photo4.zoom(3)	
    photo4 = photo4.subsample(11, 11) 
    photo5 = photo5.zoom(1)
    photo5 = photo5.subsample(8, 8) 
    photo6 = photo6.zoom(3)
    photo6 = photo6.subsample(11, 11)
    photo7 = photo7.zoom(1)	
    photo7 = photo7.subsample(8, 8)
    photo8 = photo8.zoom(8)	
    photo8 = photo8.subsample(11, 11)
    photo9 = photo9.zoom(1)	
    photo9 = photo9.subsample(8, 8)
    photo10 = photo10.zoom(10)	
    photo10 = photo10.subsample(11, 11)
    startPhoto = startPhoto.zoom(2)
    startPhoto = startPhoto.subsample(11, 11)

	#Set image on button
    tkinter.Button(root, text = 'Click Me !', command=pressedOne,
					image = photo1, highlightcolor="cyan").place(x=35, y=150)
    tkinter.Button(root, text = 'Click Me !', command=pressedTwo, 
					image = photo2).place(x=200, y=100)
    tkinter.Button(root, text = 'Click Me !', command=pressedThree,
					image = photo3).place(x=390, y=50)
    tkinter.Button(root, text = 'Click Me !', command=pressedFour,
					image = photo4).place(x=600, y=100)
    tkinter.Button(root, text = 'Click Me !', command=pressedFive, 
					image = photo5).place(x=800, y=150)
    tkinter.Button(root, text = 'Click Me !', command=pressedSix, 
					image = photo6).place(x=30, y=400)
    tkinter.Button(root, text = 'Click Me !', command=pressedSeven, 
					image = photo7).place(x=210, y=450)
    tkinter.Button(root, text = 'Click Me !', command=pressedEight, 
					image = photo8).place(x=400, y=500)
    tkinter.Button(root, text = 'Click Me !', command=pressedNine, 
					image = photo9).place(x=580, y=450)
    tkinter.Button(root, text = 'Click Me !', command=pressedTen, 
					image = photo10).place(x=780, y=400)
	
	#Start button
    tkinter.Button(root, text = 'Let\'s Begin!', command=startNumbers, 
					image = startPhoto).place(x=440, y=330)	
					
    root.wm_title("Matching Numbers")
    root.geometry("1000x750")
    root.mainloop()


if __name__== '__main__':
    main()