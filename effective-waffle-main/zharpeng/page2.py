from tkinter import *
from stupidArtnet import StupidArtnet
import time
import random
from playsound import playsound

#playsound('bgmusic.mp3')

target_ip = '192.168.1.80'    # typically in 2.x or 10.x range
universe = 0                    # see docs
packet_size = 512

def lightup():
    a = StupidArtnet(target_ip, universe, packet_size, 30, True, True)

    packet = bytearray(packet_size)
    for x in range(20):
        for i in range(packet_size):    # Fill buffer with random stuff
            packet[i] = 100
    a.set(packet) 
    time.sleep(.1)
    a.show()
    a.start()
    # a.stop()

def topagethree(): 
    # main.destroy()
    import page3

main = Tk()  #main is a variable that store tkinter 
main.title('Face-Off') 
main.state('zoom')

title = Label(main, text="Choose your theme", font=(500))
title.grid(row=0, column=0)  #widget position 

startbtn = Button(main, text="Kpop", font=(100), command=topagethree)
startbtn.grid(row=1, column=0)

main.mainloop()