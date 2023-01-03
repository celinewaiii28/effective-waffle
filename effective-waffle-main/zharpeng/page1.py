from tkinter import *
from winsound import SND_ASYNC
from playsound import playsound
from pathlib import Path 

def topagetwo(): 
    # main.destroy()
    import page2
    
def play():
    #playsound('bgmusic.mp3')
    audio = Path().cwd() / "bgmusic.mp3"
    playsound(audio, SND_ASYNC) 

    



main = Tk()  #main is a variable that store tkinter 
main.title('Face-Off') 
main.state('zoom')


title = Label(main, text="WELCOME TO FACE OFF", font=(500),)
title.grid(row=0, column=0)  #widget position 

startbtn = Button(main, text="Start", font=(100), command=topagetwo)
startbtn.grid(row=1, column=0)

# making a button which trigger the function so sound can be playeed
play_button = Button(main, text="Play Song", font=(100),    
                     relief=GROOVE, command=play)
#play_button.pack(pady=20)
play_button.grid(row=2, column=0)

main.mainloop()