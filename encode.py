import face_recognition
from pathlib import Path
import numpy as np 
import pickle 

def kfemale():
    print("Loop here!")

    with open("dict/kpopfemale", "rb") as fp:
        dict = pickle.load(fp)
    
    image = face_recognition.load_image_file("resizedIMG.png")
    face = face_recognition.face_encodings(image)

    buffer = []
    for i in range(13):
        compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
        buffer.append(compare)

    result = []

    for i in range(13):
        convert = np.array(buffer[i])
        box = (convert.tolist())
        result.append(box[0])
    
    list = []
    for i in range(13):
        count = 0
        for x in result[i]:
            if x == True:
                count = count + 1
        list.append(int(count))

    global maxindex
    maxindex = list.index(max(list))
    print("list is {}".format(list))
    print(maxindex)

    return(maxindex)


def kmale():
    print("Loop here!")

    with open("dict/kpopmale", "rb") as fp:
        dict = pickle.load(fp)
    
    image = face_recognition.load_image_file("resizedIMG.png")
    face = face_recognition.face_encodings(image)

    buffer = []
    for i in range(17):
        compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
        buffer.append(compare)

    result = []

    for i in range(17):
        convert = np.array(buffer[i])
        box = (convert.tolist())
        result.append(box[0])
    
    list = []
    for i in range(17):
        count = 0
        for x in result[i]:
            if x == True:
                count = count + 1
        list.append(int(count))

    global maxindex
    maxindex = list.index(max(list))
    print("list is {}".format(list))
    print(maxindex)

    return(maxindex)


def hmale():
    print("Loop here!")

    with open("dict/heromale", "rb") as fp:
        dict = pickle.load(fp)
    
    image = face_recognition.load_image_file("resizedIMG.png")
    face = face_recognition.face_encodings(image)

    buffer = []
    for i in range(20):
        compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
        buffer.append(compare)

    result = []

    for i in range(20):
        convert = np.array(buffer[i])
        box = (convert.tolist())
        result.append(box[0])
    
    list = []
    for i in range(20):
        count = 0
        for x in result[i]:
            if x == True:
                count = count + 1
        list.append(int(count))

    global maxindex
    maxindex = list.index(max(list))
    print("list is {}".format(list))
    print(maxindex)

    return(maxindex)


def hfemale():
    print("Loop here!")

    with open("dict/herofemale", "rb") as fp:
        dict = pickle.load(fp)
    
    image = face_recognition.load_image_file("resizedIMG.png")
    face = face_recognition.face_encodings(image)

    buffer = []
    for i in range(10):
        compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
        buffer.append(compare)

    result = []

    for i in range(10):
        convert = np.array(buffer[i])
        box = (convert.tolist())
        result.append(box[0])
    
    list = []
    for i in range(10):
        count = 0
        for x in result[i]:
            if x == True:
                count = count + 1
        list.append(int(count))

    global maxindex
    maxindex = list.index(max(list))
    print("list is {}".format(list))
    print(maxindex)

    return(maxindex)