import face_recognition
from pathlib import Path
import numpy as np

# content = np.loadtxt('kpoptestfolder/dict0.txt')
# print(content)

# file = open("kpoptestfolder/dict0.txt", "r")
# content = file.read()
# print(content)
# print(type(content))


# file = open("kpoptestfolder/dict.txt", "r")
# content = np.loadtxt("kpoptestfolder/dict.txt")
# print(content)

# with open("kpoptestfolder/dict.txt", 'r') as f:
#     contents = f.read()
# print(contents)

# # print(contents)
# # print(type(contents))]

# # print(contents)
# # print(type(contents))
# dict = []
# with open ("kpoptestfolder/dict.txt") as textFile:
#     for line in textFile:
#         value = [item.strip() for  item in line.split('[    ')]
#         dict.append(value)

# print(dict)

# dict = []
# file = open("kpoptestfolder/dict1.txt", "r")
# content = file.read()
# for sub in content: 
#     dict.append(sub.replace("", ""))

# print(dict)
# dict = list(content.split(","))
# print(dict)

dict = [] 
file = open("kpoptestfolder/dict0.txt", "r")
buffer = file.read()
content = list(buffer.split(","))
print(content)