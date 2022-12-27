import face_recognition
from pathlib import Path
from PIL import ImageTk, Image
import numpy as np 
import pickle 


def kfemale():
    print("Loop here!")

    with open("dict/kpopfemale", "rb") as fp:
        dict = pickle.load(fp)
    
    # print(dict)

    image = face_recognition.load_image_file("saved_img.png")
    face = face_recognition.face_encodings(image)
    # print("Face encoding is \n{}".format(face))

    buffer = []
    for i in range(13):
        compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
        buffer.append(compare)

    result = []

    for i in range(13):
        convert = np.array(buffer[i])
        box = (convert.tolist())
        result.append(box[0])
    
    # print("result is {}".format(result))

    list = []
    for i in range(13):
        count = 0
        for x in result[i]:
            if x == True:
                count = count + 1
        list.append(int(count))
        # print(list)

    maxindex = list.index(max(list))
    print("list is {}".format(list))
    print(maxindex)

    resultImage = Image.open("image/kpopf/image0" + str(maxindex) + ".png")
    resultImage.show()


def kmale():
    print("Loop here!")

    with open("dict/kpopmale", "rb") as fp:
        dict = pickle.load(fp)
    
    # print(dict)

    image = face_recognition.load_image_file("saved_img.png")
    face = face_recognition.face_encodings(image)
    # print("Face encoding is \n{}".format(face))

    buffer = []
    for i in range(17):
        compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
        buffer.append(compare)

    result = []

    for i in range(17):
        convert = np.array(buffer[i])
        box = (convert.tolist())
        result.append(box[0])
    
    # print("result is {}".format(result))

    list = []
    for i in range(17):
        count = 0
        for x in result[i]:
            if x == True:
                count = count + 1
        list.append(int(count))
        # print(list)

    maxindex = list.index(max(list))
    print("list is {}".format(list))
    print(maxindex)

    resultImage = Image.open("image/kpopm/image0" + str(maxindex) + ".png")
    resultImage.show()


def hmale():
    print("Loop here!")

    with open("dict/heromale", "rb") as fp:
        dict = pickle.load(fp)
    
    # print(dict)

    image = face_recognition.load_image_file("saved_img.png")
    face = face_recognition.face_encodings(image)
    # print("Face encoding is \n{}".format(face))

    buffer = []
    for i in range(17):
        compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
        buffer.append(compare)

    result = []

    for i in range(17):
        convert = np.array(buffer[i])
        box = (convert.tolist())
        result.append(box[0])
    
    # print("result is {}".format(result))

    list = []
    for i in range(17):
        count = 0
        for x in result[i]:
            if x == True:
                count = count + 1
        list.append(int(count))
        # print(list)

    maxindex = list.index(max(list))
    print("list is {}".format(list))
    print(maxindex)

    resultImage = Image.open("image/herom/image0" + str(maxindex) + ".png")
    resultImage.show()


def hfemale():
    print("Loop here!")

    with open("dict/herofemale", "rb") as fp:
        dict = pickle.load(fp)
    
    # print(dict)

    image = face_recognition.load_image_file("saved_img.png")
    face = face_recognition.face_encodings(image)
    # print("Face encoding is \n{}".format(face))

    buffer = []
    for i in range(17):
        compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
        buffer.append(compare)

    result = []

    for i in range(17):
        convert = np.array(buffer[i])
        box = (convert.tolist())
        result.append(box[0])
    
    # print("result is {}".format(result))

    list = []
    for i in range(17):
        count = 0
        for x in result[i]:
            if x == True:
                count = count + 1
        list.append(int(count))
        # print(list)

    maxindex = list.index(max(list))
    print("list is {}".format(list))
    print(maxindex)

    resultImage = Image.open("image/herof/image0" + str(maxindex) + ".png")
    resultImage.show()