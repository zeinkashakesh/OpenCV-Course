import cv2 as cv
import numpy as np


img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap)

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('sobel x', sobelx)
cv.imshow('sobel y', sobely)

combined_sobel = cv.bitwise_or(sobelx, sobely )
cv.imshow('combined sobel', combined_sobel)


canny = cv.Canny()
cv.waitKey(0)