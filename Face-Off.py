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
                grouptitle = "Harley Quinn"
                content = """Actress: Margot Robbie
                
Harley Quinn is a character appearing in American comic books published by DC Comics. 
Quinn's origin story features her as a former psychiatrist at Gotham City's Arkham Asylum named Dr. Harleen Quinzel
who fell in love with the Joker, her patient, eventually becoming his accomplice and lover. """
            elif maxindex == 4: 
                pygame.mixer.Sound.play(dc_sound)
                grouptitle = "Wonder Women"
                content = """Actress: Gal Gadot-Varsano
                
Wonder Woman's origin story (from Golden to Bronze Age) relates that she was sculpted from clay by her mother Queen Hippolyta 
and was given a life as an Amazon, along with superhuman powers as gifts by the Greek gods. 
In 2011, DC changed her background with the retcon that she is the biological daughter of Zeus and Hippolyta, 
jointly raised by her mother and her aunts Antiope and Menalippe. """
            elif maxindex == 0: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Black Widow"
                content = """Actress: Natasha Romanoff
                
Black Widow is a fictional character appearing in American comic books published by Marvel Comics. 
Created by editor and plotter Stan Lee, scripter Don Rico, and artist Don Heck, the character debuted in Tales of Suspense #52. 
The character was introduced as a Russian spy, an antagonist of the superhero Iron Man. 
"""
            elif maxindex == 1: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Captian Marvel"
                content = """Actress: Brie Larson
                
Captain Marvel is an extraterrestrial Kree warrior who finds herself caught in the middle of an intergalactic battle between her people and the Skrulls. 
Living on Earth in 1995, she keeps having recurring memories of another life as U.S. Air Force pilot Carol Danvers. 
With help from Nick Fury, Captain Marvel tries to uncover the secrets of her past 
while harnessing her special superpowers to end the war with the evil Skrulls."""
            elif maxindex == 3: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Scarlet Witch"
                content = """Actress: Elizabeth Olsen
                
The Scarlet Witch flourished as an Avenger, despite her domineering and over-protective brother. 
As she learned more about her powers and the role of a hero, 
Wanda found herself attracted to the android Vision and the two soon declared their love for each other, 
a situation Pietro found intolerable."""
            elif maxindex == 5: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Invisible Women"
                content = """Actress: Jessica Alba
                
The formidable heroine Invisible Woman (Susan Storm) uses her powers of invisibility to protect Earth 
and acts as the leading maternal figure of the Fantastic Four. 
Susan Storm Richards overcame losing her parents at a young age to become a motherly figure to her brother."""
            elif maxindex == 6: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Jane Foster"
                content = """Actress: Natalie Portman
                
For many years, Foster was a nurse, employed by Dr. Donald Blake, Thor's first mortal host, before becoming a doctor herself. 
Foster is later revealed to be deemed worthy to wield Thor's hammer Mjolnir when the former is no longer able. 
During this period, she adopts the mantle of Thor, and joins the Avengers."""
            elif maxindex == 7: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Mystique"
                content = """Actress: Jennifer Lawrence
                
As a master deceiver and infiltrator, Mystique made her way inside mutant-related organizations, 
such as becoming the leader of Freedom Force and joining X-Factor, the Marauders, and even the X-Men. 
During Mystique's trajectory, the death of Destiny had the most tragic impact in her life."""
            elif maxindex == 8: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Lady Sif"
                content = """Actress: Jaimie Alexander
                
Lady Sif is a fearsome Asgardian warrior and a good friend of Thor and the Warriors Three. 
When Thor almost provoked a war with the Frost Giants and ended up powerless on Earth, 
Sif and her friends disobeyed the orders of their new king Loki and went to Earth to save him."""
            else: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Wasp"
                content = """Actress: Evangeline Lilly 

The Wasp is the partner of Hank Pym (also known as Ant-Man), and later became his wife. 
She is usually depicted as having the ability to shrink to a height of several centimeters, 
fly by means of insectoid wings, and fire bioelectric energy blasts."""
        else:
            var = "Theme is Marvel & DC. Gender is Male"
            maxindex = encode.hmale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/herom/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)

            if maxindex == 1: 
                pygame.mixer.Sound.play(dc_sound)
                grouptitle = "Aquaman"
                content = """Actor: Jason Momoa
                
Once home to the most advanced civilization on Earth, the city of Atlantis is now an underwater kingdom ruled by the power-hungry King Orm. 
With a vast army at his disposal, Orm plans to conquer the remaining oceanic people -- and then the surface world. 
Standing in his way is Aquaman, Orm's half-human, half-Atlantean brother and true heir to the throne. 
With help from royal counselor Vulko, Aquaman must retrieve the legendary Trident of Atlan and embrace his destiny as protector of the deep."""
            elif maxindex == 2: 
                pygame.mixer.Sound.play(dc_sound)
                grouptitle = "Batman"
                content = """Actor: Ben Affleck
                
Batman ventures into Gotham City's underworld when a sadistic killer leaves behind a trail of cryptic clues. 
As the evidence begins to lead closer to home and the scale of the perpetrator's plans become clear, he must forge new relationships, 
unmask the culprit and bring justice to the abuse of power and corruption that has long plagued the metropolis."""
            elif maxindex == 6: 
                pygame.mixer.Sound.play(dc_sound)
                grouptitle = "Flash"
                content = """Actor: Ezra Miller
                
After being struck by lightning and being affected by particle-accelerator explosion, 
Barry Allen wakes up with incredible speed. He calls himself The Flash. 
Now he is desperate to find the person that killed his mother when he was a child."""
            elif maxindex == 9: 
                pygame.mixer.Sound.play(dc_sound)
                grouptitle = "Peace Maker"
                content = """Actor: John Cena
                
Peacemaker is an HBO Max-exclusive action comedy drama television series created by James Gunn and based on the DC Comics anti-hero of the same name. 
Synopsis. Peacemaker is a live action series that follows Christopher Smith AKA Peacemaker, 
an extremist murderer who believes he's on a quest for peace, killing anyone and everyone to achieve his ultimate goal."""
            elif maxindex == 12: 
                pygame.mixer.Sound.play(dc_sound)
                grouptitle = "Superman"
                content = """Actor: Henry Cavill
                
Superman is the archetype of the superhero: he wears an outlandish costume, uses a codename, and fights evil with the aid of extraordinary abilities. 
Although there are earlier characters who arguably fit this definition, it was Superman who popularized the superhero genre and established its conventions.
Superman is a fictional character and one of the most famous and popular comic book superheroes of all time."""
            elif maxindex == 0: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Antman"
                content = """Actor: Paul Rudd
                
Forced out of his own company by former protégé Darren Cross, Dr. Hank Pym (Michael Douglas) recruits the talents of Scott Lang (Paul Rudd), 
a master thief just released from prison. Lang becomes Ant-Man, trained by Pym and armed with a suit that allows him to shrink in size, 
possess superhuman strength and control an army of ants. The miniature hero must use his new skills to prevent Cross, 
also known as Yellowjacket, from perfecting the same technology and using it as a weapon for evil."""
            elif maxindex == 3: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Winter Soldier"
            elif maxindex == 4: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Captian American"
            elif maxindex == 5: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Deadpool "
            elif maxindex == 7: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Iron Man"
            elif maxindex == 8: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Moon Knight"
            elif maxindex == 10: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Spider Man"
            elif maxindex == 11: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Star Lord"
            elif maxindex == 13: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Thor"
            elif maxindex == 14: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Wolderine"
            elif maxindex == 15: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Agent Coulson"
            elif maxindex == 16: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Hawkeye"
            elif maxindex == 17: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Hulk"
            elif maxindex == 18: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Minster Fantastic"
            else: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Loki"

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