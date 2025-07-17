import cv2 as cv
import numpy as np

img=cv.imread('Photos/park.jpg')


b,g,r= cv.split(img)
blank = np.zeros(b.shape, dtype='uint8')

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)


blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])



#cv.imshow('Merged', merged)

cv.imshow('Blue Channel', blue)
cv.imshow('Green Channel', green)
cv.imshow('Red Channel', red)

cv.waitKey(0)
