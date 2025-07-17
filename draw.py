import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)


#color the blank pic
blank[:]=0,255,0
cv.imshow('Green',blank)

#color part of the pixels
blank[200:300,300:400]=0,0,255
cv.imshow('Red',blank)

#draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1)
cv.imshow('Rectangle',blank)
cv.waitKey(0)

#Draw a circle
cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
cv.imshow('Circle',blank)
cv.waitKey(0)

#draw a line

cv.line(blank,(0,0),(250,250),(255,0,0),thickness=5)
cv.imshow('Line',blank)
cv.waitKey(0)

#write text 
cv.putText(blank,'Hello World',(255,255),cv.FONT_HERSHEY_TRIPLEX,1,(0,255,255),2)
cv.imshow('Text',blank)
cv.waitKey(0)