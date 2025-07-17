import cv2 as cv

img = cv.imread('Photos/cat.jpg')

#converting to grayscale

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)


#blur
#types of blurring (Anisotropic Diffusion,Mean,box,Gaussian,Median,Bilateral,Non-Local Means)

blur= cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT) 


#Edge Cascade, it detects the edges in the image
#by blurring the image before canny, it reduces the number of edges detected
#125 is the lower threshold and 175 is the upper threshold
#if less than 125, it is not an edge, if greater than 175, it is an edge
#if between 125 and 175, it is an edge if it is connected to an edge
canny= cv.Canny(img,125,175)


#Dilation,when we the canny image, it thickens the edges
#As you increase the size of the kernel, the edges become thicker
dilated= cv.dilate(canny,(7,7),iterations=3)



#eroding, it removes the edges
#The opposite of dilation
eroded= cv.erode(dilated,(7,7),iterations=3)


#resize images
resized= cv.resize(img,(1000,1000),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropping

cropped= img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)