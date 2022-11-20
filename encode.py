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

# print(dict)

buffer=[]; result=[] #to create a list to put in a list of list 
# buffer[] is to store all result 
# result[] is to store wanted result 

for i in range(4):
    # buffer.append(dict) #a list of numpy array of list
    convert = np.array(dict[i]) #numpy array of list
    box = (convert.tolist()) #list
    result.append(box)

# print(result)
# print(type(result))

for i in range(4):
  saveimage = image = face_recognition.load_image_file('jennie_02.png') 
  ensaveimg = face_recognition.face_encodings(saveimage) #encode the saved img
  convert2 = np.array(ensaveimg)
#  box2 = (convert2.tolist())
  result1 = face_recognition.compare_faces(result, convert2[0], tolerance=0.03)

# print(result1)
# print(type(result1))

for i in range(4):
    nparray = np.array(result1)
    total = max(nparray)

print(total)
print(nparray)