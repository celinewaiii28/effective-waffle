from tkinter import * 
from PIL import Image, ImageTk 
import encode
from stupidArtnet import StupidArtnet
import time
import pygame
import sys
import os

target_ip = '192.168.1.80'
universe = 0         
packet_size = 100

def lightup():
    a = StupidArtnet(target_ip, universe, packet_size, 30, True, False)
    packet = bytearray(packet_size)

    for x in range(20):
        for i in range(packet_size):
            packet[i] = 35
        a.set(packet)
        time.sleep(.1)
        a.start()
        a.show()

def sound():
  pygame.mixer.Sound.play(sound_effect)
    
def soundStop():
  pygame.mixer.Sound.stop(sound_effect)
    
def kpop():
  pygame.mixer.Sound.play(sound_kpop)
     
def kpopStop():
  pygame.mixer.Sound.stop(sound_kpop)
  pygame.mixer.Sound.play(sound_effect)
     
def hero():
  pygame.mixer.Sound.play(sound_hero)
  
def heroStop():
  pygame.mixer.Sound.stop(sound_hero)
  pygame.mixer.Sound.play(sound_effect)
  
def camera():
  pygame.mixer.Sound.play(sound_camera)
     
     
pygame.init()
sound_effect = pygame.mixer.Sound('bgmusic.wav')
sound_effect.set_volume(1.0)
sound_kpop =  pygame.mixer.Sound('kpop.wav')
sound_kpop.set_volume(0.5)
sound_hero = pygame.mixer.Sound('superhero.wav')
sound_camera = pygame.mixer.Sound('click.wav')

def restart():
  python = sys.executable
  os.execl(python, python, * sys.argv)

def start():
    global lbl
    var = "Choose your Theme!"
    lbl.config(text=var)

    startbtn.destroy()
    theme1.pack()
    theme2.pack()

def choose_theme(m):
    global lbl, thm 
    thm = m
    var = "Choose your gender!"
    lbl.config(text=var)

    theme1.destroy()
    theme2.destroy()
    gen1.pack()
    gen2.pack()

def choose_gender(m):
    global lbl, thm, gen
    gen = m  
    var = "Click the button below to activate the camera"
    lbl.config(text=var)

    gen1.destroy()
    gen2.destroy()
    cam.pack()

def takepic():
    import camera

    global lbl
    var = "Are you ready to see the result?"
    lbl.config(text=var)

    cam.destroy()
    restartbtn.pack()

def result():
    global lbl, thm, gen, resultIMG, face

    img = (Image.open("saved_img.png"))
    resize = img.resize((500,600))
    resize.save("resizedIMG.png")

    face = ImageTk.PhotoImage(Image.open("resizedIMG.png"))
    showresized = Label(frame1, image=face)
    showresized.pack()

    if thm == 0:
        if gen == 0:
            var = "Theme is Kpop. Gender is Female"
            maxindex = encode.kfemale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/kpopf/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)
        else:
            var = "Theme is Kpop. Gender is Male"
            maxindex = encode.kmale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/kpopm/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)
    else:
        if gen == 0:
            var = "Theme is Marvel & DC. Gender is Female"
            maxindex = encode.hfemale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/herof/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)
        else:
            var = "Theme is Marvel & DC. Gender is Male"
            maxindex = encode.hmale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/herom/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)

    lbl.config(text=var)

    showresult.pack(side=LEFT)

main = Tk()
main.title("Face-Off")
# main.state('zoom')

topframe = Frame(main) # for title and btns 
topframe.pack()
ramdom = Frame(main) # for output photos
ramdom.pack()
frame1 = Frame(ramdom)
frame1.pack(side=LEFT)
frame2 = Frame(ramdom)
frame2.pack(side=LEFT)

thm = 0; gen=0

var = "Welcome to Face-Off"
title = ("Fixedsys", 40)  #Courier
btnfont = ("Courier", 20)  #Fixedsys

lbl = Label(topframe, text=var, font=title)
lbl.pack()

startbtn = Button(topframe, text="Start", font=btnfont, command= lambda : [start(), sound(), lightup()])
startbtn.pack()

theme1 = Button(topframe, text="Kpop", font=btnfont, command=lambda m=0:[choose_theme(m), kpop(), soundStop()])
theme2 = Button(topframe, text="Marvel & DC", font=btnfont, command=lambda m=1:[choose_theme(m), hero(), soundStop()])

gen1 = Button(topframe, text="Female", font=btnfont, command=lambda m=0:choose_gender(m))
gen2 = Button(topframe, text="Male", font=btnfont, command=lambda m=1:choose_gender(m))

cam = Button(topframe, text="Camera", font=btnfont, command= lambda : [takepic(), camera(), result()])

restartbtn = Button(topframe, text="Restart", font=btnfont, command=restart)

main.mainloop()