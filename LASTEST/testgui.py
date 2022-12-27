from tkinter import * 
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from itertools import count
import sys
import os

def takepic():
    import camera

# def kpopfemale():
#   import encode
#   encode.kfemale()

# def kpopmale():
#   import encode
#   encode.kmale()

# def herofemale():
#   import encode
#   encode.hfemale()

# def heromale():
#   import encode
#   encode.hmale()

def choose_theme(m):
  print("you have chosen {}".format(m))
  import encode 
  if m == 0:
    encode.kfemale()
  else:
    encode.kmale()

def chooseGender(g):
  # global labelr

  import encode
  if g == 0:
    encode.kfemale()
  elif g == 1:
    encode.kmale()
  elif g == 2:
    encode.hmale()
  else:
    encode.hfemale()

  print("you have chosen {}".format(g))


def restart():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

LARGEFONT =("Verdana", 35)
BTNFONT =('Helvetica', 16)

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
    for F in (StartPage, Page1, Page2, Page3, Page4):

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


# first window frame startpage 
class StartPage(tk.Frame):

  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    
    # # label of frame Layout 2
    # label = ttk.Label(self, text ="Welcome to FACE-OFF!", font = LARGEFONT)
    # label.grid(row = 0, column = 0, padx = 150, pady = 50)

    label = ImageLabel(self)
    # label.grid(rowspan=2, column=0)
    label.pack(expand=True, fill="both")
    label.load('homePage.gif')

    button1 = ttk.Button(self, text ="Start",
    command = lambda : controller.show_frame(Page1))
    # button1.grid(row = 1, column = 0, padx = 150, pady = 30)
    button1.pack()

# second window frame page1 / choose theme
class Page1(tk.Frame):
  
  def __init__(self, parent, controller):
    
    tk.Frame.__init__(self, parent)

    label = ttk.Label(self, text ="Choose Your Theme!", font = LARGEFONT)
    label.grid(row = 0, column = 0, padx = 150, pady = 20)

    button1 = ttk.Button(self, text ="Kpop",
    command = lambda : controller.show_frame(Page2))
    button1.grid(row = 1, column = 0, padx = 150, pady = 20)

    button2 = ttk.Button(self, text ="Marvel & DC",
    command = lambda : controller.show_frame(Page2))
    button2.grid(row = 2, column = 0, padx = 150, pady = 20)

# third window frame page2 / camera
class Page2(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)

    label = ttk.Label(self, text ="Take a photo", font = LARGEFONT)
    label.grid(row = 0, column = 0, padx = 150, pady = 20)

    button1 = ttk.Button(self, text ="Camera",
    command = lambda : [takepic(), controller.show_frame(Page3)])
    button1.grid(row = 1, column = 0, padx = 20, pady = 20)

    button2 = ttk.Button(self, text ="Back",
    command = lambda : controller.show_frame(Page1))
    button2.grid(row = 2, column = 0, padx = 10, pady = 20)


# third window frame page3 / gender for kpop
class Page3(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)

    label = ttk.Label(self, text ="Choose Your Gender", font = LARGEFONT)
    label.grid(row = 0, column = 0, padx = 150, pady = 20)

    button1 = ttk.Button(self, text ="Male",
    command = lambda g=1:chooseGender(g))
    button1.grid(row = 1, column = 0, padx = 10, pady = 10)

    button2 = ttk.Button(self, text ="Female",
    command = lambda g=0:chooseGender(g))
    button2.grid(row = 2, column = 0, padx = 10, pady = 10)

    button3 = ttk.Button(self, text ="Back",
    command = lambda : controller.show_frame(Page2))
    button3.grid(row = 3, column = 0, padx = 10, pady = 10)

# third window frame page4 / gender for hero (show result)
class Page4(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)

    label = ttk.Label(self, text ="Choose Your Gender", font = LARGEFONT)
    label.grid(row = 0, column = 0, padx = 150, pady = 20)

    button1 = ttk.Button(self, text ="Male",
    command = lambda g=2:chooseGender(g))
    button1.grid(row = 1, column = 0, padx = 10, pady = 10)

    button2 = ttk.Button(self, text ="Female",
    command = lambda g=3:chooseGender(g))
    button2.grid(row = 2, column = 0, padx = 10, pady = 10)

    button3 = ttk.Button(self, text ="Back",
    command = lambda : controller.show_frame(Page3))
    button3.grid(row = 3, column = 0, padx = 10, pady = 10)

    ####
    # import rtwo 
    # new = rtwo.maxindex

    # original = ImageTk.PhotoImage(Image.open("saved_img400.png"))
    # showresize = Label(self, image=original)
    # showresize.grid(row=4, column=0)

    # result = ImageTk.PhotoImage(Image.open("image/kpopf/image0" + str(new) + ".png"))
    # showresult = Label(self, image=result)
    # showresult.grid(row=4, column=1)


# # show result page - kpopfemale
# class Page5(tk.Frame):
#   def __init__(self, parent, controller):
#     tk.Frame.__init__(self, parent)
#     labelr = ttk.Label(self, text ="Show my result", font = LARGEFONT)
#     labelr.grid(row = 0, column = 0, padx = 150, pady = 20)

#     button1 = ttk.Button(self, text ="Result")
#     button1.grid(row = 1, column = 0, padx = 10, pady = 10)

#     ## button to restart program
#     button2 = ttk.Button(self, text ="Restart",
#     command = lambda : restart())
#     button2.grid(row = 2, column = 0, padx = 10, pady = 10)

#     button3 = ttk.Button(self, text ="Back",
#     command = lambda : controller.show_frame(Page3))
#     button3.grid(row = 3, column = 0, padx = 10, pady = 10)


# # show result page - kpopmale
# class Page10(tk.Frame):
#   def __init__(self, parent, controller):
#     tk.Frame.__init__(self, parent)
#     label = ttk.Label(self, text ="Show my result", font = LARGEFONT)
#     label.grid(row = 0, column = 0, padx = 150, pady = 20)

#     button1 = ttk.Button(self, text ="Result",
#     command = lambda : kpopmale())
#     button1.grid(row = 1, column = 0, padx = 10, pady = 10)

#     ## button to restart program
#     button2 = ttk.Button(self, text ="Restart",
#     command = lambda : restart())
#     button2.grid(row = 2, column = 0, padx = 10, pady = 10)

#     button3 = ttk.Button(self, text ="Back",
#     command = lambda : controller.show_frame(Page3))
#     button3.grid(row = 3, column = 0, padx = 10, pady = 10)

# # show result page - herofemale
# class Page6(tk.Frame):
#   def __init__(self, parent, controller):
#     tk.Frame.__init__(self, parent)
#     label = ttk.Label(self, text ="Show my result", font = LARGEFONT)
#     label.grid(row = 0, column = 0, padx = 150, pady = 20)

#     button1 = ttk.Button(self, text ="Result",
#     command = lambda : herofemale())
#     button1.grid(row = 1, column = 0, padx = 10, pady = 10)

#     ## button to restart program
#     button2 = ttk.Button(self, text ="Restart",
#     command = lambda : restart())
#     button2.grid(row = 2, column = 0, padx = 10, pady = 10)

#     button3 = ttk.Button(self, text ="Back",
#     command = lambda : controller.show_frame(Page3))
#     button3.grid(row = 3, column = 0, padx = 10, pady = 10)


# # show result page - heromale
# class Page7(tk.Frame):
#   def __init__(self, parent, controller):
#     tk.Frame.__init__(self, parent)
#     label = ttk.Label(self, text ="Show my result", font = LARGEFONT)
#     label.grid(row = 0, column = 0, padx = 150, pady = 20)

#     button1 = ttk.Button(self, text ="Result",
#     command = lambda : heromale())
#     button1.grid(row = 1, column = 0, padx = 10, pady = 10)

#     ## button to restart program
#     button2 = ttk.Button(self, text ="Restart",
#     command = lambda : restart())
#     button2.grid(row = 2, column = 0, padx = 10, pady = 10)

#     button3 = ttk.Button(self, text ="Back",
#     command = lambda : controller.show_frame(Page3))
#     button3.grid(row = 3, column = 0, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
# app.attributes('-fullscreen', True)
app.mainloop()