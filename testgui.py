from tkinter import *

heading = ("Verdana", 35)

def raise_frame(frame):
    frame.tkraise()

def takepic():
    import camera

def showresult():
    import new

root = Tk()
root.state('zoom')

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0)

Label(f1, text='Welcome to FACE-OFF', font=heading).pack()
Button(f1, text='Start', command=lambda:raise_frame(f2)).pack(padx = 10, pady = 10)

Label(f2, text='Choose a theme', font=heading).pack()
Button(f2, text='Kpop', command=lambda:raise_frame(f3)).pack(padx = 10, pady = 10)

Label(f3, text='Take a photo', font=heading).pack()
Button(f3, text='Camera', command=lambda: [takepic(), raise_frame(f4)]).pack(padx = 10, pady = 10)

Label(f4, text='Show my result', font=heading).pack()
Button(f4, text='Result', command=lambda: showresult()).pack(padx = 10, pady = 10)
Button(f4, text='Restart', command=lambda:raise_frame(f1)).pack(padx = 10, pady = 10)

raise_frame(f1)
# root.attributes('-fullscreen', True)
root.mainloop()