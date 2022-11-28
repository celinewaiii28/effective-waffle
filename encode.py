# this python file is to save the pre encoded data to a txt file

import face_recognition
from pathlib import Path
from PIL import Image
import numpy as np 


dict = []

for i in range(32): #loop the file in the folder
    fromfolder = face_recognition.load_image_file("kpoptestfolder/image0" + str(i) + ".png")
    toencode =face_recognition.face_encodings(fromfolder)
    dict.append(toencode)

with open('C:\Github\effective-waffle\encoded.txt', 'w') as fp: 
    fp.write("%s\n" % dict)

print(len(dict))
 