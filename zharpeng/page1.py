from tkinter import *
from winsound import SND_ASYNC
from playsound import playsound
#from pathlib import Pat
import pygame

def topagetwo(): 
    # main.destroy()
    import page2
    
# def play():
#     pygame.mixer.music.load('bgmusic.mp3')
#     pygame.mixer.music.play()

def sound():
    pygame.mixer.Sound.play(sound_effect)

pygame.init()
sound_effect = pygame.mixer.Sound('bgmusic.wav')     



main = Tk()  #main is a variable that store tkinter 
main.title('Face-Off') 
main.state('zoom')


title = Label(main, text="WELCOME TO FACE OFF", font=(500),)
title.grid(row=0, column=0)  #widget position 

startbtn = Button(main, text="Start", font=(100), command=topagetwo)
startbtn.grid(row=1, column=0)

# making a button which trigger the function so sound can be playeed
play_button = Button(main, text="Play Song", font=(100),    
                     relief=GROOVE, command=sound)
#play_button.pack(pady=20)
play_button.grid(row=2, column=0)

main.mainloop()