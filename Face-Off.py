from tkinter import * 
from PIL import Image, ImageTk 
import encode

def start():
    global lbl
    var = "Choose your Theme!"
    lbl.config(text=var)

    startbtn.destroy()
    theme1.grid(row=1, column=0)
    theme2.grid(row=1, column=1)

def choose_theme(m):
    global lbl, thm 
    thm = m
    var = "Choose your gender!"
    lbl.config(text=var)

    theme1.destroy()
    theme2.destroy()
    gen1.grid(row=1, column=0)
    gen2.grid(row=1, column=1)

def choose_gender(m):
    global lbl, thm, gen
    gen = m  
    var = "Take a photo of your face now"
    lbl.config(text=var)

    gen1.destroy()
    gen2.destroy()
    cam.grid(row=1, columnspan=2)

def takepic():
    import camera

    global lbl
    var = "Are you ready to see the result?"
    lbl.config(text=var)

    # img = (Image.open("saved_img.png"))
    # resize = img.resize((500,600))
    # resize.save("resizedIMG.png")

    cam.destroy()
    result.grid(row=1, columnspan=2)

def result():
    global lbl, thm, gen, resultIMG

    img = (Image.open("saved_img.png"))
    resize = img.resize((500,600))
    resize.save("resizedIMG.png")

    face = ImageTk.PhotoImage(Image.open("resizedIMG.png"))
    showresized = Label(frame1, image=face)
    showresized.grid(row=0, column=0)

    if thm == 0:
        if gen == 0:
            var = "Theme is Kpop. Gender is Female"
            maxindex = encode.kfemale()
            resultIMG = ImageTk.PhotoImage(Image.open("image/kpopf/image0" + str(maxindex) + ".png"))
            showresult = Label(frame2, image=resultIMG)
            # face = ImageTk.PhotoImage(Image.open("resizedIMG.png"))
            # showresized = Label(frame1, image=face)
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

    # img = (Image.open("saved_img.png"))
    # resize = img.resize((500,600))
    # resize.save("resizedIMG.png")

    # face = ImageTk.PhotoImage(Image.open("resizedIMG.png"))
    # showresized = Label(frame1, image=face)
    # showresized.grid(row=0, column=0)

    showresult.grid(row=0, column=1) 

main = Tk()
main.title("Face-Off")

frame1 = Frame(main)
frame1.grid(row=2, column=0)
frame2 = Frame(main)
frame2.grid(row=2, column=1)

thm = 0; gen=0

var = "Welcome to Face-Off"
title = ("Arial", 15)

lbl = Label(main, text=var, font=title)
lbl.grid(row=0, columnspan=2)

startbtn = Button(main, text="Start", command=start)
startbtn.grid(row=1, columnspan=2)

theme1 = Button(main, text="Kpop", command=lambda m=0:choose_theme(m))
theme2 = Button(main, text="Marvel & DC", command=lambda m=1:choose_theme(m))

gen1 = Button(main, text="Female", command=lambda m=0:choose_gender(m))
gen2 = Button(main, text="Male", command=lambda m=1:choose_gender(m))

cam = Button(main, text="Camera", command=takepic)

result = Button(main, text="Result", command=result)

# face = ImageTk.PhotoImage(Image.open("resizedIMG.png"))
# showresized = Label(frame1, image=face)

main.mainloop()