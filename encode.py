# this python file is to pre encode the image folder and filter out wanted result 

import face_recognition
from pathlib import Path
from PIL import Image
import numpy as np 

# this is a list to store the array with 128 list (encoded images)
dict = []

<<<<<<< Updated upstream
for i in range(14): #loop the png file in the folder 
=======
for i in range(4): #loop the file in the folder
>>>>>>> Stashed changes
    fromfolder = face_recognition.load_image_file("kpoptestfolder/image00" + str() + ".png")
    toencode =face_recognition.face_encodings(fromfolder)
    dict.append(toencode)
# print(dict)

<<<<<<< Updated upstream
imagee = face_recognition.load_image_file('saved_img-final.png')
face = face_recognition.face_encodings(imagee)

buffer=[]; result=[] 
# buffer[] is to store all results 
# result[] is to store final result that we want (True / False)
=======
# print(dict)
>>>>>>> Stashed changes

# for i in range(14):
#     convert = np.array(dict) # convert list of numpy array of list > numpy array of list 
#     box = (convert.tolist()) # numpy array of list > list 

<<<<<<< Updated upstream
# # print(box)

for i in range(14):
    # compare = face_recognition.compare_faces(['saved_img.png'], dict[0] , tolerance=0.03)
    buffer.append(dict)
    convert = np.array(buffer[i])
    box = (convert.tolist())
    # result.append(box[0])
    
result = face_recognition.compare_faces(face, box, tolerance=0.03)


print(result)
print(type(result))

=======
for i in range(4):
    # compare = face_recognition.compare_faces(['jennie_02.png'], result , tolerance=0.03)
    # buffer.append(dict) #a list of numpy array of list
    convert = np.array(dict[i]) #numpy array of list
    box = (convert.tolist()) #list
    result.append(box)

# print(result)
# print(type(result))
>>>>>>> Stashed changes

for i in range(4):
  saveimage = image = face_recognition.load_image_file('jennie_02.png') 
  ensaveimg = face_recognition.face_encodings(saveimage) #encode the saved img
  convert2 = np.array(ensaveimg)
#   box2 = (convert2.tolist())
  result1 = face_recognition.compare_faces(result, convert2[0], tolerance=0.03)

# print(result1)
# print(type(result1))

for i in range(4):
    nparray = np.array(result1)
    total = sum(nparray[i])

print(total)
print(nparray)

