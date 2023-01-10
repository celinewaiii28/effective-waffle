from tkinter import * 
from PIL import Image, ImageTk 
import encode
import sys
import os 
from stupidArtnet import StupidArtnet
import time
import pygame

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

def result():
    global lbl, thm, gen, resultIMG, face, grouptitle, content

    img = (Image.open("saved_img.png"))
    resize = img.resize((500,600))
    resize.save("resizedIMG.png")

    face = ImageTk.PhotoImage(Image.open("resizedIMG.png"))
    showresized = Label(frame1, image=face)
    popup.pack()
    showresized.pack()

    if thm == 0:
        if gen == 0:
            var = "Theme is Kpop. Gender is Female"
            maxindex = encode.kfemale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/kpopf/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)

            if maxindex == 0: 
                pygame.mixer.Sound.play(twice_sound)
                grouptitle = "JYP Entertainment, Twice"
                content = """Stage Name: Mina (미나)
Birth Name: Myoui Mina (名井 南)
English Name: Sharon
Birthday: March 24, 1997
Nationality: Japanese
Position: Main Dancer, Sub Vocalist 
Birthday: March 24, 1997

She auditioned for a JYP audition in Japan and joined the trainee program in South Korea on January 2, 2014.
She is the member who had the shortest training period before debuting as a member of Twice."""
            elif maxindex == 1: 
                pygame.mixer.Sound.play(twice_sound)
                grouptitle = "JYP Entertainment, Twice"
                content = """Stage Name: Dahyun (다현)
Birth Name: Kim Da Hyun (김다현)
English Name: Sharon
Nationality: Korean 
Position: Lead Rapper, Sub Vocalist
Birthday: May 28, 1998
                
In middle school, she performed a solo in a youth dance festival and was scouted by JYP Entertainment.
She passed the audition on July 7, 2012, and officially became a trainee.
She auditioned for SM, JYP, and YG as the same time and got accepted by all 3 companies, but she chose JYP."""
            elif maxindex == 3: 
                pygame.mixer.Sound.play(twice_sound)
                grouptitle = "JYP Entertainment, Twice"
                content = """Stage Name: Tzuyu (쯔위)
Birth Name: Chou Tzuyu (周子瑜)
Korean Name: Chou Tzu Yu (저우쯔위/주자유)
English Name: Sally
Nationality: Taiwanese
Position: Lead Dancer, Sub Vocalist, Visual
Birthday: June 14, 1999

She was discovered by JYP at the MUSE Performing Arts Workshop in Tainan in 2012 
and went to South Korea on November 15 to start her training.
She is the youngest and the tallest member in the group. """
            elif maxindex == 7: 
                pygame.mixer.Sound.play(twice_sound)
                grouptitle = "JYP Entertainment, Twice"
                content = """Stage Name: Sana (사나)
Birth Name: Minatozaki Sana (湊崎 紗夏)
Nationality: Japanese
Position: Sub Vocalist
Birthday: December 29, 1996

Sana got cast while she was shopping with her friends.
She passed the audition on April 13, 2012.
Sana is ranked 46th on TC Candler “The 100 Most Beautiful Faces of 2018", 
48 in “Most beautiful faces of 2019”, 
29th on TC Candler The most beautiful faces of 2020."""
            elif maxindex == 2: 
                pygame.mixer.Sound.play(bp_sound)
                grouptitle = "YG Entertainment, Blackpink"
                content = """Stage Name: Jennie (제니)
Birth Name: Kim Jennie (김제니)
Nationality: Korean
Position: Main Rapper, Lead Vocalist
Birthday: January 16, 1996

She trained for 5 years 11 months, (2010 August).
Jennie was the first member to be revealed (publicly).
Jennie is ranked 13th on TC Candler “The 100 Most Beautiful Faces of 2018”, 
19th on TC Candler “The 100 Most Beautiful Faces of 2019”, 
30th on TC Candler’s “The 100 Most Beautiful Faces of 2021”."""
            elif maxindex == 9: 
                pygame.mixer.Sound.play(bp_sound)
                grouptitle = "YG Entertainment, Blackpink"
                content = """Stage Name: Jisoo (지수)
Birth Name: Kim Jisoo (김지수)
Nationality: Korean
Position: Lead Vocalist, Visual
Birthday: January 3, 1995

She trained for 5 years (2011 July).
Jisoo was the third member to be revealed (publicly).
Jisoo is a white belt in taekwondo.
Jisoo ranked 78th on TC Candler “The 100 Most Beautiful Faces of 2019”, 
26th on TC Candler’s “The 100 Most Beautiful Faces of 2021”."""
            elif maxindex == 10: 
                pygame.mixer.Sound.play(bp_sound)
                grouptitle = "YG Entertainment, Blackpink"
                content = """Stage Name: Lisa (리사)
Birth Name: Pranpriya Manoban (ปราณปริยา มโนบาล) [Legalized to Lalisa Manoban (ลลิสา มโนบาล)]
Nationality: Thai
Position: Main Dancer, Lead Rapper, Sub Vocalist
Birthday: March 27, 1997

She was the only person accepted to YG in the YG Audition in Thailand 2010.
She trained for 5 years 3 months (2011 April).
Lisa is ranked 9th on TC Candler “The 100 Most Beautiful Faces of 2018”, 
3rd on TC Candler “The 100 Most Beautiful Faces of 2019”, 
2nd on TC Candler “The 100 Most Beautiful Faces of 2020”, 
1st on TC Candler “The 100 Most Beautiful Faces of 2021”.
She’s debuted as a soloist on September 10, 2021 with first single album “Lalisa”."""                
            elif maxindex == 11: 
                pygame.mixer.Sound.play(bp_sound)
                grouptitle = "YG Entertainment, Blackpink"
                content = """Stage Name: Rosé (로제)
Birth Name: Roseanne Park
Korean Name: Park Chaeyoung (박채영)
Nationality: Australian
Position: Main Vocalist, Lead Dancer
Birthday: February 11, 1997

Rosé was the last member to be revealed.
She trained for 4 years 2 months (2012 May).
Rosé ranked 66th on TC Candler “The 100 Most Beautiful Faces of 2019”.
Rosé ranked 17th on TC Candler’s “The 100 Most Beautiful Faces of 2021”.
Rosé debuted as a soloist on March 12, 2021, with first single album ‘-R-‘."""
            elif maxindex == 4: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Cube Entertainment, (G)I-DLE"
                content = """Stage Name: Soyeon (소연)
Birth Name: Jeon So Yeon (전소연)
Nationality: Korean
Position: Leader, Main Rapper, Sub Vocalist, Center
Birthday: August 26, 1998

South Korean rapper, singer, songwriter, and record producer signed to Cube Entertainment. 
First debuted as a solo-artist on November 5, 2017 
with her digital single “JELLY” which was written, composed and arranged by herself.
On May 2, 2018, she debuted as the leader and main rapper of the girl group (G)I-dle for whom she has written and produced most title songs."""
            elif maxindex == 5: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Cube Entertainment, (G)I-DLE"
                content = """Stage Name: Yuqi (우기)
Birth Name: Song Yu Qi (宋雨琦/송우기)
Korean Name: Song Woo Gi (송우기)
Nationality: Chinese
Position: Lead Dancer, Sub Vocalist, Sub Rapper, Face of the Group
Birthday: September 23, 1999

A Chinese singer, songwriter, record producer and dancer. 
She is active as a soloist in China and is a part of the South Korean girl group (G)I-dle, which debuted in 2018.
Yuqi debuted as a soloist on May 13, 2021 with single album “A Page”.
Yuqi has been nominated for “Most 100 Beautiful Faces of 2018″, representing China
"""
            elif maxindex == 6: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Cube Entertainment, (G)I-DLE"
                content = """Stage Name: Minnie (민니)
Birth Name: Nicha Yontararak (ณิชา ยนตรรักษ์)
Korean Name: Kim Min Hee (김민희)
Nationality: Thai
Position: Main Vocalist
Birthday: October 23, 1997

A Thai singer, songwriter, and actress based in South Korea.
She is a member of South Korean girl group (G)I-dle, which debuted on May 2, 2018 under Cube Entertainment.
She was born into a musical family, with her mother, aunt and uncle playing the piano.
Minnie has been playing piano since she was five and taking vocal lessons since she was seven years old.
Her mom was her main influence for loving music. """
            elif maxindex == 8: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Cube Entertainment, (G)I-DLE"
                content = """Stage Name: Shuhua (슈화)
Birth Name: Yeh Shuhua (葉舒華)
Korean Name: Yoo Su Hwa (유수화)
Nationality: Taiwanese
Position: Sub Vocalist, Visual
Birthday: January 6, 2000

On April 10, 2018, Shuhua was revealed as the third member of (G)I-DLE.
The group officially debuted on May 2 with their first mini album I Am.
She is the youngest member of the South Korean girl group (G)I-dle under Cube Entertainment. 
"""
            else: 
                pygame.mixer.Sound.play(gidle_sound)
                grouptitle = "Cube Entertainment, (G)I-DLE"
                content = """Stage Name: Miyeon (미연)
Birth Name: Cho Mi Yeon (조미연)
Nationality: Korean
Position: Main Vocalist, Visual
Birthday: January 31, 1997

She is the main vocalist of the South Korean girl group (G)I-dle under Cube Entertainment
Was known to be a YG Trainee but left YG Entertainment in 2015..
Supposed to debut with BlackPink.
She officially debuted as a soloist on April 27th, 2022.
"""
        else:
            var = "Theme is Kpop. Gender is Male"
            maxindex = encode.kmale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/kpopm/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)

            if maxindex == 0: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Big Hit Entertainment, BTS"

            elif maxindex == 1: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Big Hit Entertainment, BTS"

            elif maxindex == 2: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Big Hit Entertainment, BTS"

            elif maxindex == 3: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Big Hit Entertainment, BTS"

            elif maxindex == 6: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Big Hit Entertainment, BTS"
                
            elif maxindex == 4: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"

            elif maxindex == 5: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"

            elif maxindex == 7: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"

            elif maxindex == 8: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"

            elif maxindex == 9: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"

            elif maxindex == 10: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"

            elif maxindex == 11: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"

            elif maxindex == 12: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"

            elif maxindex == 13: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"

            elif maxindex == 14: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"

            elif maxindex == 15: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"

            else: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
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

def pop():
    global content, grouptitle

    top = Toplevel(main)
    top.title(grouptitle)
    Label(top, text=content, font=("Courier", 15)).pack()

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

startbtn = Button(topframe, text="Start", font=btnfont, command=start)
startbtn.pack()

theme1 = Button(topframe, text="Kpop", font=btnfont, command=lambda m=0:choose_theme(m))
theme2 = Button(topframe, text="Marvel & DC", font=btnfont, command=lambda m=1:choose_theme(m))

gen1 = Button(topframe, text="Female", font=btnfont, command=lambda m=0:choose_gender(m))
gen2 = Button(topframe, text="Male", font=btnfont, command=lambda m=1:choose_gender(m))

cam = Button(topframe, text="Camera", font=btnfont, command=lambda : [takepic(), result()])

grouptitle = ""
content = ""
popup = Button(topframe, text="Press Me", font=btnfont, command=pop)

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

main.mainloop()