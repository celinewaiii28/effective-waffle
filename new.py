import face_recognition
from pathlib import Path
from tkinter import * 
from PIL import ImageTk, Image
import numpy as np 
import pickle 

main = Tk()
main.title("Face-Off")

with open("dict", "rb") as fp: 
    dict = pickle.load(fp)

# print(dict)
# print("\n")
# print(type(dict))

image = face_recognition.load_image_file('saved_img.png')
face = face_recognition.face_encodings(image)

buffer = []
for i in range(30):  
    compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
    buffer.append(compare)

result=[] 

for i in range(30):
    convert = np.array(buffer[i])  
    box = (convert.tolist()) 
    result.append(box[0])

list = [] # this list is to store the count int 

for i in range(30): 
   count = 0  #loop count here so the count = 0 everytime it loop
   for x in result[i]:  # this for loop is to count the number of true in each array 
      if x == True: 
         count = count + 1
        #  print("Type of count is ", type(count))
   list.append(count)

maxindex = list.index(max(list)) # get the position of the index in the list by maximum value 
print("Position with maximum number of True in the list: ", maxindex)

frame1 = Frame(main)
frame1.grid(row=1, column=0)

frame2 = Frame(main)
frame2.grid(row=1, column=1)

words = Label(frame1, text="this is frame1")
words.grid(row=0, column=0)

w2 = Label(frame2, text="this is frame2")
w2.grid(row=0, column=0)

# original = Image.open("saved_img.png")
# original.show()

original = ImageTk.PhotoImage(Image.open("saved_img.png"))
showori = Label(frame1, image=original)
showori.grid(row=0, column=0)

# final = Image.open("kpop/image0" + str(maxindex) + ".png") #open img of the index with maximun value 
# final.show() #show image

final = ImageTk.PhotoImage(Image.open("kpop/image0" + str(maxindex) + ".png")) #open img of the index with maximun value 
showfinal = Label(frame2, image=final) #show image
showfinal.grid(row=0, column=0)

main.mainloop()