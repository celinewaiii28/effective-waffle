import face_recognition
from pathlib import Path
from PIL import Image
import numpy as np 
import pickle 

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
original = Image.open("saved_img.png")
original.show()
final = Image.open("kpop/image0" + str(maxindex) + ".png") #open img of the index with maximun value 
final.show() #show image