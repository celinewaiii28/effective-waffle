# this python file is to pre encode the image folder and filter out wanted result 

import face_recognition
from pathlib import Path
from PIL import Image
import numpy as np 


dict = []

for i in range(4): #loop the file in the folder
    fromfolder = face_recognition.load_image_file("kpoptestfolder/image0" + str(i) + ".png")
    toencode =face_recognition.face_encodings(fromfolder)
    dict.append(toencode)

buffer = []
image = face_recognition.load_image_file('test.png')
face = face_recognition.face_encodings(image)

for i in range(4): 
    compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
    buffer.append(compare)

# print(buffer)

result=[] #to create a list to put in a list of list 

for i in range(4):
    convert = np.array(buffer[i])
    # print(convert)
    box = (convert.tolist())
    # print(box)
    result.append(box[0])

# print("result is {}".format(result))
# print(result)

list = []
# count = 0 
for i in range(4): 
   count = 0
   for x in result[i]: 
      if x == True: 
         count = count + 1
        #  print(count)
   list.append(count)
    
print(list)

maxindex = list.index(max(list))
print("Position with maximum number of True in the list: ", maxindex)

final = Image.open("kpoptestfolder/image0" + str(maxindex) + ".png")
final.show()

