import face_recognition
from pathlib import Path
from PIL import Image
import numpy as np 

dict = []

for i in range(32): 
    loadImage = face_recognition.load_image_file("kpoptestfolder/image0" + str(i) + ".png")
    encodeImage = face_recognition.face_encodings(loadImage)
    file = open("dict/dict" + str(i) + ".txt", "w")
    # predict = np.array(encodeImage)
    file.write(str(encodeImage))
    file.close()
    # dict.append(encodeImage)
# print(dict)



# file = open("kpoptestfolder/dict.txt", "w+")
# predict = np.array(dict)
# content = str(predict)
# file.write(content)
# file.close()


# with open("kpoptestfolder/dict.txt", 'w') as f:
# #     f.write(str(dict))

# with open('kpoptestfolder/dict.txt', 'w') as filehandle:
#     for listitem in dict:
#         filehandle.write('%s\n'%listitem)

# image = Image.open(loadImage)
# image = Image.open("kpoptestfolder/image00.png")
# image.show()

