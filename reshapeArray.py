import face_recognition
<<<<<<< Updated upstream

imagehq = face_recognition.load_image_file("rose_08.png")
face1 =face_recognition.face_encodings(imagehq)
print("Face 1")
print(face1)

imagehq = face_recognition.load_image_file("seventeendk_20.png")
face2 =face_recognition.face_encodings(imagehq)
print("Face 2")
print(face2[1])

# # import required module
# from pathlib import Path

# # get the path/directory
# folder_dir = 'Kpop'

# # iterate over files in
# # that directory
# images = Path(folder_dir).glob('*.png')
# for image in images:
# 	face = face_recognition.face_encodings(image)

=======
import os
from pathlib import Path
from face_recognition.face_recognition_cli import image_files_in_folder

# get the path/directory
my_dir = 'Kpop/'
encoding_for_file = []
for i in os.listdir(my_dir):
    image = my_dir + i
    image = face_recognition.load_image_file(image)
    image_encoding = face_recognition.face_encodings(image)
    # encoding_for_file.append(image_encoding[0])
    print(image_encoding)

# folder_dir = 'Kpop'

# images = Path(folder_dir).glob('*.png')
# for i in images:
#     # check if the image ends with png
#         image = face_recognition.load_image_file(i)
#         faceEncode = face_recognition.face_encodings(image)
#         print(faceEncode)

# imagehq = face_recognition.load_image_file("seventeendk_20.png")
# facehq =face_recognition.face_encodings(imagehq)
# print(face1)
>>>>>>> Stashed changes


imagenic = face_recognition.load_image_file("saved_img.png")
facenic =face_recognition.face_encodings(imagenic)

# print("Nic = ",facenic)
# print("Antman = ", faceam)
# print("HQ = ", facehq)

<<<<<<< Updated upstream
result1 = face_recognition.compare_faces([face2, face1], facenic[0], tolerance=0.08)
=======
# result1 = face_recognition.compare_faces([image_encoding], facenic[0], tolerance=0.03)
>>>>>>> Stashed changes
# print(result1)

# array1 = np.array(result1[0])

# print(type(result1[0]))
# count = 0

# for x in result1[0]: 
#     if x == True: 
#         # print(x)
#         count = count + 1

<<<<<<< Updated upstream
print(" 2 = ", count)
=======
# print(" 0 = ", count)
>>>>>>> Stashed changes
    
# count = 0
# for y in result1[1]: 
#     if y == True: 
#         # print(y)
#         count = count + 1
# print("1 = " , count)

