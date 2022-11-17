import face_recognition

imagehq = face_recognition.load_image_file("rose_08.png")
face1 =face_recognition.face_encodings(imagehq)
print("Face 1")
print(face1)

imagehq = face_recognition.load_image_file("seventeendk_20.png")
face2 =face_recognition.face_encodings(imagehq)
print("Face 2")
print(face2)

# # import required module
# from pathlib import Path

# # get the path/directory
# folder_dir = 'Kpop'

# # iterate over files in
# # that directory
# images = Path(folder_dir).glob('*.png')
# for image in images:
# 	face = face_recognition.face_encodings(image)



imagenic = face_recognition.load_image_file("saved_img.png")
facenic =face_recognition.face_encodings(imagenic)

# print("Nic = ",facenic)
# print("Antman = ", faceam)
# print("HQ = ", facehq)

result1 = face_recognition.compare_faces([face2, face1], facenic[0], tolerance=0.08)
# print(result1)

# array1 = np.array(result1[0])

# print(type(result1[0]))
count = 0

for x in result1[0]: 
    if x == True: 
        # print(x)
        count = count + 1

print(" 2 = ", count)
    
count = 0
for y in result1[1]: 
    if y == True: 
        # print(y)
        count = count + 1
print("1 = " , count)

