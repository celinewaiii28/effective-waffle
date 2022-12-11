from tkinter import * 

def topagethree(): 
    # main.destroy()
    import page3

main = Tk()  #main is a variable that store tkinter 
main.title('Face-Off') 
main.state('zoom')

title = Label(main, text="Choose your theme", font=(500))
title.grid(row=0, column=0)  #widget position 

startbtn = Button(main, text="Kpop", font=(100), command=topagethree)
startbtn.grid(row=1, column=0)

main.mainloop()