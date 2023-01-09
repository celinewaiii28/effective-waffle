import face_recognition
import pickle 

kpopFemale = [] 
for i in range(13): #loop the file in the folder
    fromfolderkpopf = face_recognition.load_image_file("image/kpopf/image0" + str(i) + ".png")
    toencode1 = face_recognition.face_encodings(fromfolderkpopf)
    kpopFemale.append(toencode1)

kpopMale = [] 
for i in range(17): #loop the file in the folder
    fromfolderkpopm = face_recognition.load_image_file("image/kpopm/image0" + str(i) + ".png")
    toencode2 = face_recognition.face_encodings(fromfolderkpopm)
    kpopMale.append(toencode2)

heroFemale = []
for i in range (20):
    fromfolderherof = face_recognition.load_image_file("image/herof/image0" + str(i) + ".png")
    toencode3 = face_recognition.face_encodings(fromfolderherof)
    heroFemale.append(toencode3)

heroMale = []
for i in range (10):
    fromfolderherom = face_recognition.load_image_file("image/herom/image0" + str(i) + ".png")
    toencode4 = face_recognition.face_encodings(fromfolderherof)
    heroMale.append(toencode4)

#kpop female
with open("dict/kpopfemale", "wb") as fp:
    pickle.dump(kpopFemale, fp)

with open("dict/kpopfemale", "rb") as fp: 
    encoded = pickle.load(fp)

#kpopmale
with open("dict/kpopmale", "wb") as fp:
    pickle.dump(kpopMale, fp)

with open("dict/kpopmale", "rb") as fp: 
    encoded = pickle.load(fp)

#hero female
with open("dict/herofemale", "wb") as fp:
    pickle.dump(heroFemale, fp)

with open("dict/herofemale", "rb") as fp: 
    encoded = pickle.load(fp)

#hero male
with open("dict/heromale", "wb") as fp:
    pickle.dump(heroMale, fp)

with open("dict/heromale", "rb") as fp: 
    encoded = pickle.load(fp)

# print(encoded)
# print(type(encoded))