from tkinter import *
from tkVideoPlayer import TkinterVideo

def loopVideo(event):
    videoplayer.play()

root = Tk()

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(r"homePage.gif")
videoplayer.pack(expand=True, fill="both")

home = videoplayer.play() # play the video

label1 = Label(root, image=home)
label1.place(x=0, y=0)

videoplayer.bind('<<Ended>>', loopVideo)
root.mainloop()