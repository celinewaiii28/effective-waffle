import face_recognition
import pickle 

dict = [] 
for i in range(30): #loop the file in the folder
    fromfolder = face_recognition.load_image_file("kpop/image0" + str(i) + ".png")
    toencode = face_recognition.face_encodings(fromfolder)
    dict.append(toencode)

# print(dict)

with open("dict", "wb") as fp:
    pickle.dump(dict, fp)

with open("dict", "rb") as fp: 
    encoded = pickle.load(fp)

print(encoded)
print(type(encoded))