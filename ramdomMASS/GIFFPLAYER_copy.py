from tkinter import * 
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import sys
import os

import tkinter as tk
from PIL import Image, ImageTk
from itertools import count

def takepic():
    import camera

def showresult():
  import new
  new.guiResult()

def restart():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

LARGEFONT =("Verdana", 35)
BTNFONT =('Helvetica', 16)

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

class tkinterApp(tk.Tk):
  
  # __init__ function for class tkinterApp
  def __init__(self, *args, **kwargs):
    
    # __init__ function for class Tk
    tk.Tk.__init__(self, *args, **kwargs)
    
    # creating a container
    container = tk.Frame(self)
    container.pack(side = "top", fill = "both", expand = True)

    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)

    # initializing frames to an empty array
    self.frames = {}

    # iterating through a tuple consisting
    # of the different page layouts
    for F in (StartPage, Page1, Page2, Page3):

      frame = F(container, self)

      # initializing frame of that object from
      # startpage, page1, page2 respectively with
      # for loop
      self.frames[F] = frame

      frame.grid(row = 0, column = 0)

    self.show_frame(StartPage)

  # to display the current frame passed as
  # parameter
  def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()

# first window frame startpage 
class StartPage(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    
    # label of frame Layout 2
    #label = ttk.Label(self, text ="Welcome to FACE-OFF!", font = LARGEFONT)
    #label.grid(row = 0, column = 0, padx = 50, pady = 40)

    button1 = ttk.Button(self, text ="Start",
    command = lambda : controller.show_frame(Page1))
    button1.grid(row = 1, column = 0, padx = 20, pady = 30)

# second window frame page1 / choose theme
class Page1(tk.Frame):
  
  def __init__(self, parent, controller):
    
    tk.Frame.__init__(self, parent)

    label = ttk.Label(self, text ="Choose Your Theme!", font = LARGEFONT)
    label.grid(row = 0, column = 0, padx = 100, pady = 40)

    button1 = ttk.Button(self, text ="Kpop",
    command = lambda : controller.show_frame(Page2))
    button1.grid(row = 1, column = 0, padx = 20, pady = 10)


# third window frame page2 / camera
class Page2(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)

    label = ttk.Label(self, text ="Take a photo", font = LARGEFONT)
    label.grid(row = 0, column = 0, padx = 100, pady = 50)

    button1 = ttk.Button(self, text ="Camera",
    command = lambda : [takepic(), controller.show_frame(Page3)])
    button1.grid(row = 1, column = 0, padx = 10, pady = 10)



class Page3(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    label = ttk.Label(self, text ="Show my result", font = LARGEFONT)
    label.grid(row = 0, column = 0, padx = 100, pady = 40)

    button1 = ttk.Button(self, text ="Result",
    command = lambda : showresult())
    button1.grid(row = 1, column = 1, padx = 60, pady = 10)
    button1.grid(row = 1, column = 0, padx = 60, pady = 10)

    ## button to restart program
    button2 = ttk.Button(self, text ="Restart",
    command = lambda : restart())
    button2.grid(row = 2, column = 0, padx = 20, pady = 10)


root = tkinterApp()
root.geometry("1000x1000")
lbl = ImageLabel(root)
lbl.pack()
lbl.load('homePage.gif')
root.mainloop()
