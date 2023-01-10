from tkinter import * 
from PIL import Image, ImageTk 
import encode
import sys
import os 
from stupidArtnet import StupidArtnet
import time
import pygame
import cv2

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

def start():
    global lbl
    var = "Choose Your Theme!"
    lbl.config(text=var)

    startbtn.destroy()
    lbl.pack()
    theme1.pack()
    theme2.pack()

    pygame.mixer.Sound.play(bg_sound)


def choose_theme(event, m=''):
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
    var = "Take a photo of your face now"
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

    pygame.mixer.Sound.stop(bg_sound)
    pygame.mixer.Sound.play(cam_sound)
    
def instruct():
  pygame.mixer.Sound.play(instruct_sound)

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

            if maxindex == 0: 
                pygame.mixer.Sound.play(twice_sound)
            elif maxindex == 1: 
                pygame.mixer.Sound.play(twice_sound)
            elif maxindex == 3: 
                pygame.mixer.Sound.play(twice_sound)
            elif maxindex == 7: 
                pygame.mixer.Sound.play(twice_sound)
            elif maxindex == 2: 
                pygame.mixer.Sound.play(bp_sound)
            elif maxindex == 9: 
                pygame.mixer.Sound.play(bp_sound)
            elif maxindex == 10: 
                pygame.mixer.Sound.play(bp_sound)
            elif maxindex == 11: 
                pygame.mixer.Sound.play(bp_sound)
            else: 
                pygame.mixer.Sound.play(gidle_sound)
        else:
            var = "Theme is Kpop. Gender is Male"
            maxindex = encode.kmale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/kpopm/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)

            if maxindex == 0: 
                pygame.mixer.Sound.play(bts_sound)
            elif maxindex == 1: 
                pygame.mixer.Sound.play(bts_sound)
            elif maxindex == 2: 
                pygame.mixer.Sound.play(bts_sound)
            elif maxindex == 3: 
                pygame.mixer.Sound.play(bts_sound)
            elif maxindex == 6: 
                pygame.mixer.Sound.play(bts_sound)
            else: 
                pygame.mixer.Sound.play(seven_sound)
    else:
        if gen == 0:
            var = "Theme is Marvel & DC. Gender is Female"
            maxindex = encode.hfemale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/herof/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)

            if maxindex == 2: 
                pygame.mixer.Sound.play(dc_sound)
            elif maxindex == 4: 
                pygame.mixer.Sound.play(dc_sound)
            else: 
                pygame.mixer.Sound.play(marvel_sound)
        else:
            var = "Theme is Marvel & DC. Gender is Male"
            maxindex = encode.hmale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/herom/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)

            if maxindex == 1: 
                pygame.mixer.Sound.play(dc_sound)
            elif maxindex == 2: 
                pygame.mixer.Sound.play(dc_sound)
            elif maxindex == 6: 
                pygame.mixer.Sound.play(dc_sound)
            elif maxindex == 9: 
                pygame.mixer.Sound.play(dc_sound)
            elif maxindex == 12: 
                pygame.mixer.Sound.play(dc_sound)
            else: 
                pygame.mixer.Sound.play(marvel_sound)

    lbl.config(text=var)

    showresult.pack(side=LEFT)

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

main = Tk()
main.title("Face-Off")
# main.state('zoom')

topframe = Frame(main) # for title and btns 
topframe.pack()
ramdom = Frame(main) # for output photos
ramdom.pack()
frame1 = Frame(ramdom)  # face photo
frame1.pack(side=LEFT)
frame2 = Frame(ramdom)  # result photo
frame2.pack(side=LEFT)

thm = 0; gen=0

var = "Welcome to Face-Off"
title = ("Fixedsys", 40)  #Courier
btnfont = ("Courier", 20)  #Fixedsys

lbl = Label(topframe, text=var, font=title)
lbl.pack()

# themebg = PhotoImage(file="theme.png")
# bg1 = Label(main, image=themebg)
# bg1.pack()

#main.bind('<d>', lambda event : choose_theme(m))

startbtn = Button(topframe, text="Start", font=btnfont, command=start)
startbtn.pack()


theme1 = Button(topframe, text="Kpop", font=btnfont, command=lambda m=0:choose_theme(m))
theme2 = Button(topframe, text="Marvel & DC", font=btnfont, command=lambda m=1:choose_theme(m))

    

gen1 = Button(topframe, text="Female", font=btnfont, command=lambda m=0:[choose_gender(m),instruct()])
gen2 = Button(topframe, text="Male", font=btnfont, command=lambda m=1:[choose_gender(m), instruct()])

cam = Button(topframe, text="Camera", font=btnfont, command=lambda : [takepic(), result()])

restartbtn = Button(topframe, text="Restart", font=btnfont, command=restart)

pygame.init()
bg_sound = pygame.mixer.Sound("soundtrack/bgmusic.wav")
cam_sound = pygame.mixer.Sound("soundtrack/click.wav")
bp_sound = pygame.mixer.Sound("soundtrack/blackpink.wav")
twice_sound = pygame.mixer.Sound("soundtrack/twice.wav")
gidle_sound = pygame.mixer.Sound("soundtrack/gidle.wav")
bts_sound = pygame.mixer.Sound("soundtrack/bts.wav")
seven_sound = pygame.mixer.Sound("soundtrack/seventeen.wav")
dc_sound = pygame.mixer.Sound("soundtrack/dc.wav")
marvel_sound = pygame.mixer.Sound("soundtrack/marvel.wav")
instruct_sound = pygame.mixer.Sound("soundtrack/instruct_camera.wav")


main.mainloop()