import face_recognition
from PIL import Image
import numpy as np

dict = []
for i in range(32):
    file = open("dict/dict" + str(i) + ".txt", "r")
    buffer = file.read()
    convert = buffer.replace(" ", "")
    convert1 = convert.replace(" ", "")
    convert2 = convert.replace("\n","")
    # print(convert2)
    dict.append(list(convert2.split(",")))
# print(dict)
# print(dict[0][0])
# print(type(dict[0][0]))
# print(type(convert2))
# var = list(convert2.split(","))
# print(type(convert2))
# print("{} \n".format(convert2))

lib = [[0.0 for j in range(128)] for i in range(32)]

for i in range(32):
    for j in range(128):
        lib[i][j] = float(dict[i][j])

# print("Lib result")
# print(lib)
# print(lib[31])
# print(lib)
# print("\n\n\n")

# num = []
# for i in range(128):
#     var = float(dict[0][i])
#     num.append(var)

# print(type(num[0]))
# print("{}\n".format(num[0]))


####
captureImage = face_recognition.load_image_file("test.png")
captureEncode = face_recognition.face_encodings(captureImage)
convert = np.array(captureEncode)
buffer = (convert.tolist())
captureResult = buffer[0]
# print(captureResult)
# print(type(captureResult[0]))
# print(len(captureResult))
####

print("Lib Result")
print("{} and type is {}\n".format(lib[0], type(lib[0])))

print("captureEncode Result")
print("{} and type is {}\n".format(captureEncode[0], type(captureEncode[0])))

buffer = face_recognition.compare_faces([lib], captureEncode[0], tolerance=0.08)
print(buffer)
# compare = []
# for i in range(32):
#     buffer = face_recognition.compare_faces(lib[i], captureResult, tolerance=0.6)
#     compare.append(buffer)

# print(compare)
