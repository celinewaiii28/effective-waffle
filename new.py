import face_recognition
from pathlib import Path
from PIL import ImageTk, Image
import numpy as np 
import pickle 

def guiResult():
    print("Loop here!")

    with open("dict", "rb") as fp:
        dict = pickle.load(fp)
    
    # print(dict)

    image = face_recognition.load_image_file("saved_img.png")
    face = face_recognition.face_encodings(image)
    # print("Face encoding is \n{}".format(face))

    buffer = []
    for i in range(30):
        compare = face_recognition.compare_faces([dict[i]], face[0], tolerance=0.08)
        buffer.append(compare)

    result = []

    for i in range(30):
        convert = np.array(buffer[i])
        box = (convert.tolist())
        result.append(box[0])
    
    # print("result is {}".format(result))

    list = []
    for i in range(30):
        count = 0
        for x in result[i]:
            if x == True:
                count = count + 1
        list.append(int(count))
        # print(list)

    maxindex = list.index(max(list))
    print("list is {}".format(list))
    print(maxindex)

    # resultImage = Image.open("kpop/image0" + str(maxindex) + ".png")
    # resultImage.show()

    pictaken = Image.open("saved_img.png")

    size = (200, 300)

    output = pictaken.resize(size)

    output.save('resized-saved-img.png')
