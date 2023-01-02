from tkinter import * 
from PIL import Image, ImageTk 
import encode

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
    result.pack()

def result():
    global lbl, thm, gen, resultIMG

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
main.state('zoom')

topframe = Frame(main)
topframe.pack(side=TOP)
frame1 = Frame(main)
frame1.pack(side=LEFT)
frame2 = Frame(main)
frame2.pack(side=RIGHT)

thm = 0; gen=0

var = "Welcome to Face-Off"
title = ("Arial", 15)

lbl = Label(topframe, text=var, font=title)
lbl.pack()

startbtn = Button(topframe, text="Start", command=start)
startbtn.pack()

theme1 = Button(topframe, text="Kpop", command=lambda m=0:choose_theme(m))
theme2 = Button(topframe, text="Marvel & DC", command=lambda m=1:choose_theme(m))

gen1 = Button(topframe, text="Female", command=lambda m=0:choose_gender(m))
gen2 = Button(topframe, text="Male", command=lambda m=1:choose_gender(m))

cam = Button(topframe, text="Camera", command=takepic)

result = Button(topframe, text="Result", command=result)

main.mainloop()