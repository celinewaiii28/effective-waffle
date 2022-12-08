from tkinter import * 

def camera():
    import camera
    import new


def topageone(): 
    main.destroy()
    import page1


main = Tk()  #main is a variable that store tkinter 
main.title('Face-Off')  
# main.state('zoom')

title = Label(main, text="THIS IS PAGE 3", font=(500))
title.grid(row=0, column=0)  #widget position 

camerabtn = Button(main, text="Camera", font=(100), command=camera)
camerabtn.grid(row=1, column=0)  #widget position 

resetbtn = Button(main, text="Reset", font=(100), command=topageone)
resetbtn.grid(row=1, column=1)  #widget position 

main.mainloop()
