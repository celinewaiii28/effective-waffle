from tkinter import * 

def topagetwo(): 
    main.destroy()
    import page2

main = Tk()  #main is a variable that store tkinter 
main.title('Face-Off') 
# main.state('zoom')

title = Label(main, text="WELCOME TO FACE OFF", font=(500))
title.grid(row=0, column=0)  #widget position 

startbtn = Button(main, text="Start", font=(100), command=topagetwo)
startbtn.grid(row=1, column=0)

main.mainloop()