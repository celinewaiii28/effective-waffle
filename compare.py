# this python file is to pre encode the image folder and filter out wanted result 

import face_recognition
from pathlib import Path
from PIL import Image
import numpy as np 
import ast

# dict = []

# for i in range(32): #loop the file in the folder
#     fromfolder = face_recognition.load_image_file("kpoptestfolder/image0" + str(i) + ".png")
#     toencode = face_recognition.face_encodings(fromfolder)
#     dict.append(toencode)

buffer = [] # this list is to put in the 128 array of compare faces encoding 

image = face_recognition.load_image_file('saved_img.png')
face = face_recognition.face_encodings(image)

# opening the file in read mode
my_file = open("encoded.txt", "r")

# reading the file
data = my_file.read()

# when newline ('\n') is seen.
txt = ast.literal_eval(data)

my_file.close()


# this loop is to compare_faces of the save_img.png to all files in img folder 
for i in range(32):  
    compare = face_recognition.compare_faces([txt[i]], face[0], tolerance=0.08)
    buffer.append(compare)


# # this loop is to compare_faces of the save_img.png to all files in img folder 
# for i in range(32):  
#     compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
#     buffer.append(compare)

# print("buffer = ", buffer

result=[] # this list is to store wanted result 

for i in range(32):
    convert = np.array(buffer[i])  # list of numpy array of list > numpy array of list 
    # print(convert)
    box = (convert.tolist()) # numpy array of list > list 
    # print(box)
    result.append(box[0])

# print("result is {}".format(result))
# print(result)

list = [] # this list is to store the count int 

for i in range(32): 
   count = 0  #loop count here so the count = 0 everytime it loop
   for x in result[i]:  # this for loop is to count the number of true in each array 
      if x == True: 
         count = count + 1
        #  print("Type of count is ", type(count))
   list.append(count)  #turn count(int) into a list 
    
print(list) # to check the number of True in different array 

maxindex = list.index(max(list)) # get the position of the index in the list by maximum value 
print("Position with maximum number of True in the list: ", maxindex)

final = Image.open("kpoptestfolder/image0" + str(maxindex) + ".png") #open img of the index with maximun value 
final.show() #show image