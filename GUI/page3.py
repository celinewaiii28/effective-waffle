from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('Page3')
# ws.attributes('-fullscreen',True)
ws['bg']='#5d8a82'

f = ("Times bold", 14)

def nextPage():
    ws.destroy()
    import page1

def prevPage():
    ws.destroy()
    import page2
    
Label(
    ws,
    text="This is Third page",
    padx=20,
    pady=20,
    bg='#ffbf00',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Previous Page", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws, 
    text="Next Page", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)
    
ws.mainloop()