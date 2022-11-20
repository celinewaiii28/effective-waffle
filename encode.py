# this python file is to pre encode the image folder and filter out wanted result 

import face_recognition
from pathlib import Path
from PIL import Image
import numpy as np 


dict = []

for i in range(14): #loop the file in the folder
    fromfolder = face_recognition.load_image_file("kpoptestfolder/image00" + str() + ".png")
    toencode =face_recognition.face_encodings(fromfolder)
    dict.append(toencode)

print(dict)


buffer=[]; result=[] #to create a list to put in a list of list 
# buffer[] is to store all result 
# result[] is to store wanted result 

for i in range(14):
    compare = face_recognition.compare_faces(['saved_img.png'], dict[0] , tolerance=0.03)

    buffer.append(compare)
    convert = np.array(buffer[i])
    box = (convert.tolist())
    result.append(box[0])

print(len(result[0]))


    





