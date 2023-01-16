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
    var = "Choose a Theme!"
    lbl.config(text=var)

    startbtn.destroy()
    lbl.pack()
    theme1.pack()
    theme2.pack()

    pygame.mixer.Sound.play(bg_sound)

def choose_theme(m):
    global lbl, thm 
    thm = m
    var = "Select your gender. "
    lbl.config(text=var)

    theme1.destroy()
    theme2.destroy()
    gen1.pack()
    gen2.pack()

def choose_gender(m):
    global lbl, thm, gen
    gen = m  
    var = "Press button to activate the Camera. "
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
            var = "Do you know who is she? PRESS ME to read more!"
            maxindex = encode.kfemale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/kpopf/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)

            if maxindex == 0: 
                pygame.mixer.Sound.play(twice_sound)
                pygame.mixer.Sound.fadeout(5000)
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
                pygame.mixer.Sound.play(gidle_sound)
                grouptitle = "Cube Entertainment, (G)I-DLE"
                content = """Stage Name: Soyeon (소연)
Birth Name: Jeon So Yeon (전소연)
Nationality: Korean
Position: Leader, Main Rapper, Sub Vocalist, Center
Birthday: August 26, 1998

South Korean rapper, singer, songwriter, and record producer signed to Cube Entertainment. 
First debuted as a solo-artist on November 5, 2017 
with her digital single “JELLY” which was written, composed and arranged by herself.
On May 2, 2018, she debuted as the leader and main rapper of the girl group (G)I-dle 
for whom she has written and produced most title songs."""
            elif maxindex == 5: 
                pygame.mixer.Sound.play(gidle_sound)
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
                pygame.mixer.Sound.play(gidle_sound)
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
                pygame.mixer.Sound.play(gidle_sound)
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
            var = "Do you know who is he? PRESS ME to read more! "
            maxindex = encode.kmale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/kpopm/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)

            if maxindex == 0: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Big Hit Entertainment, BTS"
                content = """Stage Name: Jungkook (정국)
Full Name: Jeon Jung Kook (전정국)
Position: Main Vocalist, Lead Dancer, Sub Rapper, Center, Maknae
Birthday: September 1, 1997

He was born in Busan, South Korea.
He has an older brother, Jeon Junghyun.
Education: Seoul School of Performing Arts; Global Cyber University
Before joining the group he was a handball player.
Hobbies: Drawing."""

            elif maxindex == 1: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Big Hit Entertainment, BTS"
                content = """Stage Name: J-Hope (제이홉)
Full Name: Jung Ho Seok (정호석)
Position: Main Dancer, Sub Rapper, Sub Vocalist
Birthday: February 18, 1994

He was born in Gwangju, South Korea.
He has an older sister known as, Mejiwoo.
His father is a high school literature teacher (teaching at Gwangju Global High School).
Education: Gwangju Global High School; Global Cyber University
Hobbies: Listening to music and window shopping."""

            elif maxindex == 2: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Big Hit Entertainment, BTS"
                content = """Stage Name: Jimin (지민)
Full Name: Park Ji Min (박지민)
Position: Main Dancer, Lead Vocalist
Birthday: October 13, 1995

He was born in Busan, South Korea.
He has a younger brother, Park Jihyun.
Education: Busan High School of Arts; Global Cyber University(Theatre and film major (bachelor))
Jimin was the last member to join BTS.
Hobbies: Relaxing whenever he gets a chance."""

            elif maxindex == 3: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Big Hit Entertainment, BTS"
                content = """Stage Name: Jin (진)
Birth Name: Kim Seok Jin (김석진)
Position: Sub Vocalist, Visual
Birthday: December 4, 1992

He was born in Anyang, Gyeonggi-do, but when he was about 1 year old his family moved to Gwacheon, Gyeonggi-do
He has an older brother, Kim Seok Joong, 2 years older than him.
Education: Konkuk University; Hanyang Cyber University (Films major (masters/graduate))
He is the oldest member.
Hobbies: Cooking, playing videogames on Nintendo devices, taking selcas."""

            elif maxindex == 6: 
                pygame.mixer.Sound.play(bts_sound)
                grouptitle = "Big Hit Entertainment, BTS"
                content = """Stage Name: RM (아르엠), formerly Rap Monster (랩몬스터)
Birth Name: Kim Nam Joon (김남준)
Position: Leader, Main Rapper
Birthday: September 12, 1994

He was born in Seoul (Sangdo-dong) then he moved to Ilsan, Gyeonggi-do, South Korea when he was 4.
Education: Apgujeong High School; Global Cyber University (Electronic engineering major (bachelor))
In 2006 RM studied languages in New Zealand for 4 months. (Bon Voyage 4 Ep 1)
He taught himself how to speak English and can speak it extremely well.
BTS has been around since 2010, but they debuted in 2013 because of the constant member change up. 
RM is the only member left from the original line up."""
                
            elif maxindex == 4: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
                content = """Stage Name: Mingyu (민규)
Birth Name: Kim Min Gyu (김민규)
Position: Rapper, Sub Vocalist, Visual, Face of the Group
Birthday: April 6, 1997
Sub-Unit: Hip-Hop Team

He was born in Anyang-si, Gyeonggi-do, South Korea.
He is the tallest member in the group.
He ranks himself #1 visuals in Hip Hop unit.
He became a trainee in 2011.
He's in charge of hair styling in the group."""

            

            elif maxindex == 5: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
                content = """Stage Name: Joshua (조슈아)
Birth Name: Joshua Hong
Korean Name: Hong Ji Soo (홍지수)
Position: Lead Vocalist, Visual
Birthday: December 30, 1995
Sub-Unit: Vocal Team

He was born in Los Angeles, California, United States.
Joshua is fully Korean but was born and raised in America.
He's an only child.
He joined Pledis Entertainment and began his training in 2013.
He said music is his life."""

            elif maxindex == 7: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
                content="""Stage Name: Wonwoo (원우)
Birth Name: Jeon Won Woo (전원우)
Position: Rapper, Sub Vocalist
Birthday: July 17, 1996
Sub-Unit: Hip-Hop Team

He was born in Changwon, Gyeongsangnam-do, South Korea
He became a trainee in 2011.
He ranks himself 3rd or 4th most handsome in the group. 
He says S.Coups is the most handsome to him because he's very manly and has good leadership.
He says he looks cold due to his sharp eyes but he's a warm person."""

            elif maxindex == 8: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
                content = """Stage Name: Hoshi (호시)
Birth Name: Kwon Soon Young (권순영)
Position: Performance Team Leader, Main Dancer, Lead Vocalist, Sub Rapper
Birthday: June 15, 1996
Sub-Unit: Performance Team (Leader)/ SVT Leaders/ BOOSEOKSOON

He was born in Namyangju-si, Gyeonggi-do, South Korea.
Hoshi's nickname is 10:10 because his eyes are the the same angles of ten minute ten hour on a clock.
He choreographs most of Seventeen's routines.
He became a trainee in 2011.
He is a black belt in Taekwondo and was a Taekwondo champion when he was young."""

            elif maxindex == 9: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
                content = """Stage name: S.Coups (에스쿱스)
Birth name: Choi Seung Cheol (최승철)
Position: Leader, Hip-Hop Team Leader, Rapper, Sub Vocalist
Birthday: August 8, 1995
Sub-Unit: Hip-Hop Team (Leader); SVT Leaders

He was born in Daegu, South Korea.
His stage name S.Coups comes from: (S) his name Sungcheol, (Coups) Coup d'état.
He became a trainee in 2010.
He's one of the original Pledis Boys."""

            elif maxindex == 10: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
                content = """Stage Name: DK / Dokyeom (도겸)
Birth Name: Lee Seok Min (이석민)
Position: Main Vocalist
Birthday: February 18, 1997
Sub-Unit: Vocal Team; BOOSEOKSOON (Leader)

He was born in Suji-gu, Yongin-si, Gyeonggi-do, South Korea.
Hansol, Seungkwan & Jisoo think he's the funniest member.
He became a trainee in 2012."""

            elif maxindex == 11: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
                content = """Stage Name: Jeonghan (정한)
Birth Name: Yoon Jeong Han (윤정한)
Position: Lead Vocalist, Visual
Birthday: October 4, 1995
Sub-Unit: Vocal Team

He was born in Hwaseong, South Korea.
He has a younger sister.
He ranks himself the third best visual in the group (after Vernon and Mingyu).
He became a trainee in 2013"""

            elif maxindex == 12: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
                content = """Stage Name: Seungkwan (승관)
Birth Name: Boo Seung Kwan (부승관)
Position: Main Vocalist, Face of the Group
Birthday: January 16, 1998
Sub-Unit: Vocal Team; BOOSEOKSOON

He was born in Busan, but he lived in Jeju since he was little.
He has 2 older sisters: Boo Jinseol, and Boo Sojeong, the latter of whom debuted as a singer in Oct 2020.
He is Seventeen's mood maker.
He became a trainee in 2012.
He was offered to join JYP but he rejected the offer."""

            

            elif maxindex == 13: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
                content = """Stage Name: Vernon (버논)
Birth Name: Hansol Vernon Chwe
Korean Name: Choi Han Sol (최한솔)
Position: Rapper, Sub Vocalist, Visual, Face of the Group
Birthday: February 18, 1998
Sub-Unit: Hip-Hop Team

He was born in New York, United States.
His family lives in Hongdae but he lives in Gangnam since Seventeen's dorm is located there.
His father is Korean and his mother is American.
He has a younger sister named Sofia, born in 2004.
He became a trainee in 2012."""

            elif maxindex == 14: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
                content = """Stage Name: The8 (디에잇)
Birth Name: Xu Ming Hao (徐明浩)
Korean Name: Seo Myung Ho (서명호)
Position: Lead Dancer, Sub Vocalist, Sub Rapper
Birthday: November 7, 1997
Sub-Unit: Performance Team

e was born in Haicheng, Liaoning, China.
He is in charge of b-boying in the performance team.
He did b-boying in China for 6 years.
He became a trainee in 2013.
The meaning behind his stage name is that when the 8 is laid down, 
the infinite sign appears. Many Chinese people like number 8."""

            elif maxindex == 15: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
                content = """Stage Name: Dino (디노)
Birth Name: Lee Chan (이찬)
Position: Main Dancer, Sub Vocalist, Sub Rapper, Maknae
Birthday: February 11, 1999
Sub-Unit: Performance Team

He was born in Iksan-si, Jeollakbu-do, South Korea.
He explained that, in a family tree, his name is written as “Lee Joong Chan” but that 
his real name is actually Lee Chan. (During an interview for tenasia.co.kr)
His parents are dancers. His father opened up a dance class and thought taught him how to dance.
He became a trainee in 2012"""

            else: 
                pygame.mixer.Sound.play(seven_sound)
                grouptitle = "Pledis Entertainment, Seventeen"
                content = """Stage Name: Jun (준)
Birth  Name: Wen Junhui (文俊辉)
Korean Name: Moon Jun Hwi (문준휘)
Position: Lead Dancer, Sub Vocalist
Birthday: June 10, 1996
Sub-Unit: Performance Team

He was born in Shenzhen, Guangdong, China.
He was a child actor in China.
He speaks Mandarin, Cantonese, Korean.
Many Chinese students love Kpop and that's how he became curious about it and moved to Korea.
He became a trainee in 2012."""

    else:
        if gen == 0:
            var = "Do you know who is she? PRESS ME to read more! "
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
                
Captain Marvel is an extraterrestrial Kree warrior who finds herself caught in the 
middle of an intergalactic battle between her people and the Skrulls. 
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
            var = "Do you know who is he? PRESS ME to read more! "
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
                
Peacemaker is an HBO Max-exclusive action comedy drama television series created by James Gunn 
and based on the DC Comics anti-hero of the same name. 
Synopsis. Peacemaker is a live action series that follows Christopher Smith AKA Peacemaker, 
an extremist murderer who believes he's on a quest for peace, killing anyone and everyone to achieve his ultimate goal."""
            elif maxindex == 12: 
                pygame.mixer.Sound.play(dc_sound)
                grouptitle = "Superman"
                content = """Actor: Henry Cavill
                
Superman is the archetype of the superhero: he wears an outlandish costume, uses a codename, 
and fights evil with the aid of extraordinary abilities. 
Although there are earlier characters who arguably fit this definition, it was Superman 
who popularized the superhero genre and established its conventions.
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
                content = """Actor: Sebastian Stan
                
After the cataclysmic events in New York with his fellow Avengers, Steve Rogers, aka Captain America, 
lives in the nation's capital as he tries to adjust to modern times. 
An attack on a S.H.I.E.L.D. colleague throws Rogers into a web of intrigue that places the whole world at risk. 
Joining forces with the Black Widow and a new ally, the Falcon, Rogers struggles to expose an ever-widening conspiracy, 
but he and his team soon come up against an unexpected enemy."""
            elif maxindex == 4: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Captian American"
                content = """Actor: Chris Evans
                
It is 1941 and the world is in the throes of war. Steve Rogers (Chris Evans) wants to do his part and join America's armed forces, 
but the military rejects him because of his small stature. Finally, Steve gets his chance when he is accepted into an experimental program 
that turns him into a supersoldier called Captain America. Joining forces with Bucky Barnes (Sebastian Stan) and Peggy Carter (Hayley Atwell), 
Captain America leads the fight against the Nazi-backed HYDRA organization."""
            elif maxindex == 5: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Deadpool"
                content = """Actor: Ryan Rodney Reynolds
                
Wade Wilson (Ryan Reynolds) is a former Special Forces operative who now works as a mercenary. 
His world comes crashing down when evil scientist Ajax (Ed Skrein) tortures, disfigures and transforms him into Deadpool. 
The rogue experiment leaves Deadpool with accelerated healing powers and a twisted sense of humor. 
With help from mutant allies Colossus and Negasonic Teenage Warhead (Brianna Hildebrand), 
Deadpool uses his new skills to hunt down the man who nearly destroyed his life."""
            elif maxindex == 7: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Iron Man"
                content = """Actor: Robert Downey Jr.
                
A billionaire industrialist and genius inventor, Tony Stark (Robert Downey Jr.), is conducting weapons tests overseas, 
but terrorists kidnap him to force him to build a devastating weapon. Instead, he builds an armored suit and upends his captors. 
Returning to America, Stark refines the suit and uses it to combat crime and terrorism."""
            elif maxindex == 8: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Moon Knight"
                content = """Actor: Oscar Isaac
                
It follows Marc Spector and Steven Grant, 
two alters of a man with dissociative identity disorder (DID), 
as they are drawn into a mystery involving Egyptian gods. """
            elif maxindex == 10: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Spider Man"
                content = """Actor: Tom Holland
                
"Spider-Man" centers on student Peter Parker who, after being bitten by a genetically-altered spider, 
gains superhuman strength and the spider-like ability to cling to any surface. He vows to use his abilities to fight crime, 
coming to understand the words of his beloved Uncle Ben: "With great power comes great responsibility."""
            elif maxindex == 11: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Star Lord"
                content = """Actor: Chris Pratt
                
Powers and abilities. Star-Lord is a master strategist and problem solver who is an expert in close-quarter combat, 
various human and alien firearms, and battle techniques. He has extensive knowledge of various alien customs, societies, and cultures, 
and considerable knowledge about cosmic abstracts, such as Oblivion."""
            elif maxindex == 13: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Thor"
                content = """Actor: Chris Hemsworth
                
Imprisoned on the other side of the universe, 
the mighty Thor finds himself in a deadly gladiatorial contest that pits him against the Hulk, 
his former ally and fellow Avenger. Thor's quest for survival leads him in a race against time to prevent the 
all-powerful Hela from destroying his home world and the Asgardian civilization."""
            elif maxindex == 14: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Wolverine"
                content = """Actor: Hugh Jackman
                
He is a mutant who possesses animal-keen senses, enhanced physical capabilities, 
a powerful regenerative ability known as a healing factor, and three retractable claws in each hand. 
Wolverine has been depicted variously as a member of the X-Men, X-Force, Alpha Flight, the Fantastic Four, and the Avengers."""
            elif maxindex == 15: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Agent Coulson"
                content = """Actor: Clark Gregg

"Phil" Coulson was a highly decorated agent and former Director of S.H.I.E.L.D.. 
Coulson was Nick Fury's right-hand man for many important missions and his liaison to the Avengers."""
            elif maxindex == 16: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Hawkeye"
                content = """Actor: Jeremy Renner

Clint BartonHawkeye. A master marksman and longtime friend of Black Widow, 
Clint Barton serves as the Avengers' amazing archer. An expert marksman and fighter, 
Clint Barton puts his talents to good use by working for S.H.I.E.L.D. as a special agent."""
            elif maxindex == 17: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Hulk"
                content = """Actor: Mark Ruffalo
                
Bruce Banner lives a life caught between the soft-spoken scientist he's always been and the 
uncontrollable green monster powered by his rage. Exposed to heavy doses of gamma radiation, 
scientist Bruce Banner transforms into the mean, green rage machine called the Hulk."""
            elif maxindex == 18: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Mister Fantastic"
                content = """Actor: Ioan Gruffudd
                
Reed Richards is a scientist and inventor, better known as Mister Fantastic, 
who has been considered the smartest man on Earth. He is a polymath with mastery of all the sciences including, 
electrical, mechanical, aerospace engineering, electronics, chemistry, physics, biology and beyond."""
            else: 
                pygame.mixer.Sound.play(marvel_sound)
                grouptitle = "Loki"
                content = """Actor: Thomas William Hiddleston
                
God of Mischief and brother to Thor, Loki's tricks and schemes wreak havoc across the realms. 
Loki, Prince of Asgard, Odinson, rightful heir of Jotunheim, and God of Mischief, is burdened with glorious purpose. 
His desire to be a king drives him to sow chaos in Asgard."""

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