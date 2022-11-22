# this python file is to pre encode the image folder and filter out wanted result 

import face_recognition
from pathlib import Path
from PIL import Image
import numpy as np 


dict = []

for i in range(14): #loop the file in the folder
    fromfolder = face_recognition.load_image_file("kpoptestfolder/image0" + str(i) + ".png")
    toencode =face_recognition.face_encodings(fromfolder)
    dict.append(toencode)

buffer = []
image = face_recognition.load_image_file('saved_img.png')
face = face_recognition.face_encodings(image)

for i in range(14): 
    compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
    buffer.append(compare)

# print("buffer = ", buffer)

result=[] # this list is to store wanted result 

for i in range(14):
    convert = np.array(buffer[i])
    # print(convert)
    box = (convert.tolist()) # numpy array of list > list 
    # print(box)
    result.append(box[0])

# print("result is {}".format(result))
# print(result)
# print(compare)

list = []
# count = 0 
for i in range(14): 
   count = 0
   for x in result[i]: 
      if x == True: 
         count = count + 1
        #  print("Type of count is ", type(count))
   list.append(count)  #turn count(int) into a list 
    
print(list) # to check the number of True in different array 

maxindex = list.index(max(list)) # get the position of the index in the list by maximum value 
print("Position with maximum number of True in the list: ", maxindex)

final = Image.open("kpoptestfolder/image0" + str(maxindex) + ".png") #open img of the index with maximun value 
final.show() #show image
