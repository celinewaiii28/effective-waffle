# this python file is to pre encode the image folder and filter out wanted result 

import face_recognition
from pathlib import Path
from PIL import Image
import numpy as np 


dict = []

for i in range(4): #loop the file in the folder
    fromfolder = face_recognition.load_image_file("kpoptestfolder/image00" + str() + ".png")
    toencode =face_recognition.face_encodings(fromfolder)
    dict.append(toencode)

buffer = []
image = face_recognition.load_image_file('jennie_02.png')
face = face_recognition.face_encodings(image)

for i in range(4): 
    compare = face_recognition.compare_faces(dict, face[0], tolerance=0.03)
    buffer.append(compare[0])

# print(buffer)

result=[] #to create a list to put in a list of list 

for i in range(4):
    convert = np.array(buffer[i])
    # print(convert)
    box = (convert.tolist())
    # print(box)
    result.append(box)

# print("result is {}".format(result))
# print(result)

count = 0 
for i in range(4): 
  for x in result[i]: 
    if x == True: 
        count = count + 1

print("True = " , count)
print(type(count))
