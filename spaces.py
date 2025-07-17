import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#bgr to hsv
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#bgr to lab
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#bgr to rgb
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)

cv.waitKey(0)