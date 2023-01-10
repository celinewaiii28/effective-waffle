from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('kpoptestfolder/image01.png')
#plt.imshow(img[:,:,::-1])
#plt.show()

result = DeepFace.analyze(img, actions=['gender'])
print("Gender : ", result['gender'])