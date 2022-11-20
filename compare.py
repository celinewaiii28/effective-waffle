# this python file is to compare and show matching image. 

import face_recognition
from pathlib import Path
from PIL import Image
import encode
# import camera


# image = face_recognition.load_image_file('saved_img.png')
saveimage = image = face_recognition.load_image_file('jennie_02.png') 
ensaveimg = face_recognition.face_encodings(saveimage) #encode the saved img

finalresult = []
for i in range(14):
    compare = face_recognition.compare_faces([encode.result], ensaveimg, tolerance=0.03)
    finalresult.append[compare]
    

print(finalresult)


#encode.result encode is the file name .result is the variable