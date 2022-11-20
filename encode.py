# this python file is to pre encode the image folder and filter out wanted result 

import face_recognition
from pathlib import Path
from PIL import Image
import numpy as np 

# this is a list to store the array with 128 list (encoded images)
dict = []

for i in range(14): #loop the png file in the folder 
    fromfolder = face_recognition.load_image_file("kpoptestfolder/image00" + str() + ".png")
    toencode =face_recognition.face_encodings(fromfolder)
    dict.append(toencode)
# print(dict)

imagee = face_recognition.load_image_file('saved_img-final.png')
face = face_recognition.face_encodings(imagee)

buffer=[]; result=[] 
# buffer[] is to store all results 
# result[] is to store final result that we want (True / False)

# for i in range(14):
#     convert = np.array(dict) # convert list of numpy array of list > numpy array of list 
#     box = (convert.tolist()) # numpy array of list > list 

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






