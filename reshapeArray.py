import face_recognition

imagehq = face_recognition.load_image_file("seventeendk_20.png")
facehq =face_recognition.face_encodings(imagehq)
# print(face1)

# imageam = face_recognition.load_image_file("miyeon_14.png")
# faceam =face_recognition.face_encodings(imageam)

imagenic = face_recognition.load_image_file("saved_img.png")
facenic =face_recognition.face_encodings(imagenic)

# print("Nic = ",facenic)
# print("Antman = ", faceam)
# print("HQ = ", facehq)

result1 = face_recognition.compare_faces([faceam, facehq], facenic[0], tolerance=0.03)
# print(result1)

# array1 = np.array(result1[0])

# print(type(result1[0]))
count = 0

for x in result1[0]: 
    if x == True: 
        # print(x)
        count = count + 1

print(" 0 = ", count)
    
count = 0
for y in result1[1]: 
    if y == True: 
        # print(y)
        count = count + 1
print("1 = " , count)

