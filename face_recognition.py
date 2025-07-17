import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier("haar_face.xml")

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
#features = np.load('features.npy', allow_pickle=True)
#labels = np.load('labels.npy', allow_pickle=True) 

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')


img = cv.imread(r'C:\Users\pc\Desktop\OpenCV course\Faces\val\ben_afflek\2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#detect the face in the image 

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

for(x,y,w,h) in faces_rect:
  faces_roi = gray[y:y+h, x:x+w]
  label, confidence = face_recognizer.predict(faces_roi)
  print(f'label= {people[label]}, confidence= {confidence}')

  cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
  cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow("Detected", img)

cv.waitKey(0)
