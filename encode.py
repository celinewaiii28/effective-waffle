# this python file is to save the pre encode value for img folder 
import face_recognition
from pathlib import Path
from PIL import Image
import numpy as np 

dict = []

for i in range(33): #loop the file in the folder
    fromfolder = face_recognition.load_image_file("kpop/image0" + str(i) + ".png")
    toencode =face_recognition.face_encodings(fromfolder)
    dict.append(toencode)

print(dict)
