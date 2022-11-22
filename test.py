import dlib
import numpy as np 
import face_recognition

image = face_recognition.load_image_file("saved_img.png")
face =face_recognition.face_encodings(image)
print(face)
