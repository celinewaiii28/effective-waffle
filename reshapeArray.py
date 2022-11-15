import dlib
import numpy as np 
import face_recognition

imagehq = face_recognition.load_image_file("XagentC_21.png")
facehq =face_recognition.face_encodings(imagehq)
# print(face1)

imageam = face_recognition.load_image_file("antman_00.png")
faceam =face_recognition.face_encodings(imageam)

imagenic = face_recognition.load_image_file("saved_img.png")
facenic =face_recognition.face_encodings(imagenic)

# print("Nic = ",facenic)
# print("Antman = ", faceam)
# print("HQ = ", facehq)

result1 = face_recognition.compare_faces([faceam, facehq], facenic[0], tolerance=0.08)
print(result1)

# array1 = np.array(result1[0])

# print(array1)