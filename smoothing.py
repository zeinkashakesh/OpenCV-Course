import cv2 as cv

img = cv.imread('Photos/cat.jpg' )
cv.imshow('Cat', img)

#Averaging
avg = cv.blur(img,(3,3))
cv.imshow("avg",avg)

#Gaussian Blur
gauss= cv.GaussianBlur(img,(3,3),0)
cv.imshow("gauss",gauss)

#Mediam Blur
median = cv.medianBlur(img,7)
cv.imshow("median",median)
cv.waitKey(0)

#Bilateral Blur 
#Bilateral filtering is a technique that reduces noise while keeping edges sharp.
bilat = cv.bilateralFilter(img,5,15,15)
cv.imshow("bilateral",bilat)