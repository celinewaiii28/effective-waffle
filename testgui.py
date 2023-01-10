from tkinter import * 
import tkinter as tk
from tkinter import ttk
import sys
import os
from stupidArtnet import StupidArtnet
import time
import random
import pygame

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
sound_kpop =  pygame.mixer.Sound('kpop.wav')
sound_kpop.set_volume(0.4)
sound_hero = pygame.mixer.Sound('superhero.wav')
sound_camera = pygame.mixer.Sound('click.wav')

target_ip = '192.168.1.80'		# typically in 2.x or 10.x range
universe = 0										# see docs
packet_size = 512

def lightup():
  a = StupidArtnet(target_ip, universe, packet_size, 30, True, True)

  packet = bytearray(packet_size)
  for x in range(20):
    for i in range(packet_size):  	# Fill buffer with random stuff
      packet[i] = 100
  a.set(packet) 
  time.sleep(.1)
  a.start()
  a.show()
  
  # a.stop()

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


# first window frame startpage 
class StartPage(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    
    # label of frame Layout 2
    label = ttk.Label(self, text ="Welcome to FACE-OFF!", font = LARGEFONT)
    label.grid(row = 0, column = 0, padx = 150, pady = 50)


    button1 = ttk.Button(self, text ="Start",
    command = lambda : [controller.show_frame(Page1),lightup(), sound()])
    button1.grid(row = 1, column = 0, padx = 150, pady = 30)
    

# second window frame page1 / choose theme
class Page2(tk.Frame):
  
  def __init__(self, parent, controller):
    
    tk.Frame.__init__(self, parent)

    label = ttk.Label(self, text ="Choose Your Theme!", font = LARGEFONT)
    label.grid(row = 0, column = 0, padx = 150, pady = 20)

    button1 = ttk.Button(self, text ="Kpop",
    command = lambda : [controller.show_frame(Page3), kpop(), soundStop()])
    button1.grid(row = 1, column = 0, padx = 150, pady = 20)

    button2 = ttk.Button(self, text ="Marvel & DC",
    command = lambda : [controller.show_frame(Page4), hero(), soundStop()])
    button2.grid(row = 2, column = 0, padx = 150, pady = 20)

# third window frame page2 / camera
class Page1(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)

    label = ttk.Label(self, text ="Take a photo", font = LARGEFONT)
    label.grid(row = 0, column = 0, padx = 150, pady = 20)

    button1 = ttk.Button(self, text ="Camera",
    command = lambda : [takepic(), camera(), controller.show_frame(Page2)])
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
    command = lambda : [controller.show_frame(Page1), kpopStop()])
    button3.grid(row = 3, column = 0, padx = 10, pady = 10)

# third window frame page4 / gender for hero
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
    command = lambda : [controller.show_frame(Page1), heroStop()])
    button3.grid(row = 3, column = 0, padx = 10, pady = 10)
  


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