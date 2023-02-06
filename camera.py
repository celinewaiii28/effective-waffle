# this python file to to capture and store img of the face

import face_recognition
import cv2
from pathlib import Path
from PIL import Image
import pygame

  
#pygame.init()

#take_photo = pygame.mixer.Sound('takephoto.wav')
#pygame.mixer.Sound.play(take_photo)

  # pygame.mixer.Sound.stop(sound_hero)
  # pygame.mixer.Sound.stop(sound_effect) 
# sound_smile = pygame.mixer.Sound('smile.wav')
# pygame.mixer.Sound.play(sound_smile)


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

key = cv2. waitKey(0)
webcam = cv2.VideoCapture(0)

while True:
        check, frame = webcam.read()
     #if there is no edge detection around the face, this text will pop up
        # text = "Press s to take picture :)"
    
    # convert each frame from BGR to Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
    # detect faces using Haar Cascade    
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        width = 500
        height = 540
        dim = (width, height)

        frame1 = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)    
        mirror= cv2.flip(frame1,1)    
    
    #  #to draw a rectangle around the face
    #     for(x, y, w, h) in faces:
    #          text = "Face33 Detected" 
    #          cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
     
        # display the text on the image
        # print(text)
        # image = cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3, cv2.LINE_AA)

        capture = key == ord('s')
        cv2.imshow('Face Detection Capture', mirror)
        try:

            # print(check) #prints true as long as the webcam is running
            # print(frame) #prints matrix values of each framecd 
            #cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if capture: 
                cv2.imwrite(filename='saved_img.png', img=frame)
                webcam.release()
                # img_new = cv2.imread('saved_img.png', cv2.IMREAD_GRAYSCALE)
                # img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                # img_ = cv2.imread('saved_img.png', cv2.IMREAD_ANYCOLOR)
                # print("Converting RGB image to grayscale...")
                # gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                # print("Converted RGB image to grayscale...")
                # print("Resizing image to 28x28 scale...")
                # img_ = cv2.resize(gray,(20,25))
                # print("Resized...")
                #img_resized = cv2.imwrite(filename='saved_img-final.png', img=img_)
                print("Image saved!")
                break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
