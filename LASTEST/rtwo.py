from tkinter import * 
import face_recognition
from pathlib import Path
from PIL import ImageTk, Image
import numpy as np 
import pickle 


def kfemale():

    main = Tk()
    main.title("Face-Off")

    print("Loop here!")

    with open("dict/kpopfemale", "rb") as fp:
        dict = pickle.load(fp)
    
    # print(dict)

    image = face_recognition.load_image_file("saved_img.png")
    face = face_recognition.face_encodings(image)

    buffer = []
    for i in range(13):
        compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
        buffer.append(compare)

    result = []

    for i in range(13):
        convert = np.array(buffer[i])
        box = (convert.tolist())
        result.append(box[0])
    
    list = []
    for i in range(13):
        count = 0
        for x in result[i]:
            if x == True:
                count = count + 1
        list.append(int(count))

    global maxindex
    maxindex = list.index(max(list))
    print("list is {}".format(list))
    print(maxindex)


    frame1 = Frame(main)
    frame1.grid(row=1, column=0)

    frame2 = Frame(main)
    frame2.grid(row=1, column=1)

    img = (Image.open("saved_img.png"))
    resize = img.resize((500,500))
    resize.save("saved_img400.png")

    original = ImageTk.PhotoImage(Image.open("saved_img400.png"))
    showresize = Label(frame1, image=original)
    showresize.grid(row=1, column=0)

    result = ImageTk.PhotoImage(Image.open("image/kpopf/image0" + str(maxindex) + ".png"))
    showresult = Label(frame2, image=result)
    showresult.grid(row=1, column=0)

    main.mainloop()