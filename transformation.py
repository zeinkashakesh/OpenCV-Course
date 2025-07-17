import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
#cv.imshow('Boston', img)

#Translation
#Is the shifting of an image in the x and y direction
#x is the number of pixels to shift in the x direction
#[1,0,x] 1# is the scale factor in the x direction, 0 is the shear factor, and x is the translation in the x direction
#[0,1,y] 0 is the shear factor in the x direction, 1 is the scale factor in the y direction, and y is the translation in the y direction
#This whole matrix is a transformation matrix that is used to shift the image
def translate(img,x,y):
  transMat = np.float32([[1,0,x],[0,1,y]])
  dimensions = (img.shape[1],img.shape[0])
  return cv.warpAffine(img,transMat,dimensions) #is responsible for the transformation of the image with respect to the affine matrix


 #Rotation
 #getRotationMatrix2D is used to get the rotation matrix,it is calculated in the function
 #if you rotate the img twice, it may lose part of the image
def rotate(img,angle,rotPoint=None):
  (height,width) = img.shape[:2]
  if rotPoint is None:
    rotPoint = (width//2,height//2)
  rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0) #The rotation matrix is created with respect to the rotation point, angle, and scale factor
  print (rotMat)
  dimensions = (width,height)
  return cv.warpAffine(img,rotMat,dimensions)


#Flipping
#flipCode = 0 is vertical flip, 1 is horizontal flip, -1 is both
flipped=cv.flip(img,-1)
  

cv.imshow("flipped",flipped)
cv.waitKey(0)