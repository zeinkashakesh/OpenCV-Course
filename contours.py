import cv2 as cv 
import numpy as np

img = cv.imread('Photos/cats.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)
#Thresholding attemnpts to binarize the image
#its is better to use canny to find contours than thresholding
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
cv.imshow('Contours', thresh)
print(f'Number of contours found: {len(contours)}')
cv.drawContours(blank, contours, -1, (0, 0, 255), thickness=0)
cv.imshow('Contours Drawn', blank)
 
"""
==============================================================
Suzuki and Abe (1985) proposed a topological analysis algorithm that can build 
a hierarchy of contours (parents, children, siblings). OpenCV exposes this
flexibility through the mode parameter:

    RETR_LIST → no hierarchy.
    RETR_TREE → full hierarchy.
    RETR_EXTERNAL → only outermost contours.
=============================================================
CHAIN_APPROX_NONE → maximum detail → every pixel along the contour.
CHAIN_APPROX_SIMPLE → simplifies horizontal/vertical/diagonal segments → reduces memory/storage.
==============================================================
"""

cv.waitKey(0)
