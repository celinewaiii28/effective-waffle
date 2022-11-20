import face_recognition
import cv2
from pathlib import Path
from PIL import Image
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

key = cv2. waitKey(0)
webcam = cv2.VideoCapture(0)

while True:
        check, frame = webcam.read()
     #if there is no edge detection around the face, this text will pop up
        text = "Face not in frame"
    
    # convert each frame from BGR to Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
    # detect faces using Haar Cascade    
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    
    
     #to draw a rectangle around the face
        # for(x, y, w, h) in faces:
        #     text = "Face Detected" 
        #     cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        
        # display the text on the image
        print(text)
        image = cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
        cv2.imshow('Face Detection Capture', frame)
        try:
            
         
            print(check) #prints true as long as the webcam is running
            print(frame) #prints matrix values of each framecd 
            #cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename='saved_img.png', img=frame)
                webcam.release()
                img_new = cv2.imread('saved_img.png', cv2.IMREAD_GRAYSCALE)
                img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                img_ = cv2.imread('saved_img.png', cv2.IMREAD_ANYCOLOR)
                print("Converting RGB image to grayscale...")
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                print("Converted RGB image to grayscale...")
                print("Resizing image to 28x28 scale...")
                img_ = cv2.resize(gray,(28,28))
                print("Resized...")
                img_resized = cv2.imwrite(filename='saved_img-final.png', img=img_)
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



# # Load the image of the person we want to find similar people for
# known_image = face_recognition.load_image_file("saved_img.png")
# # Encode the known image
# known_image_encoding = face_recognition.face_encodings(known_image)[0]


# # Variables to keep track of the most similar face match we've found
# best_face_distance = 1.0
# best_face_image = None
# # Loop over all the images we want to check for similar people
# for image_path in Path("Characters").glob("*.png"):

#     # Load an image to check
#     unknown_image = face_recognition.load_image_file(image_path)

#     # Get the location of faces and face encodings for the current image
#     face_encodings = face_recognition.face_encodings(unknown_image)

#     # Get the face distance between the known person and all the faces in this image
#     face_distance = face_recognition.face_distance(face_encodings, known_image_encoding)[0]

    

#     # If this face is more similar to our known image than we've seen so far, save it
#     if face_distance < best_face_distance:
#         # Save the new best face distance
#         best_face_distance = face_distance
#         # Extract a copy of the actual face image itself so we can display it
#         best_face_image = unknown_image
# # Display the face image that we found to be the best match!
# pil_image = Image.fromarray(best_face_image)
# pil_image.show()


