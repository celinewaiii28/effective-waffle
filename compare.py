import face_recognition
from pathlib import Path
from PIL import Image
import encode
# import camera


# image = face_recognition.load_image_file('saved_img.png')
saveimage = image = face_recognition.load_image_file('saved_img.png') 
ensaveimg = face_recognition.face_encodings(saveimage) #encode the saved img

finalresult = []
for i in range(14):
    toencode = face_recognition.compare_faces([encode.result], ensaveimg,tolerance=0.03)
    results = finalresult.append[toencode]

print(finalresult)


#encode.result encode is the file name .result is the variable