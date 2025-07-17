import cv2 as cv

def rescaleFrame(frame,scale=0.75):
  #Works for images, Videos and live videos
  width=int(frame.shape[1]*scale)
  height=int(frame.shape[0]*scale)
  dimensions=(height,width)
  return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA )
  #interpolation is for estimationg the color of the new pixels

def changeRes(width,height):
  #For live videos
  capture.set(3,width) #3 is the width
  capture.set(4,height) #4 is the height
  # 3 and 4 are the index for width and height 


img =cv.imread('Photos/cat.jpg' )
img_resized=rescaleFrame(img)
cv.imshow('Cat', img_resized)

capture= cv.VideoCapture('Videos/dog.mp4')
while True: 
  isTrue, frame = capture.read()
  frame_resized = rescaleFrame(frame)

  cv.imshow('Video', frame_resized)
  if cv.waitKey(20) & 0xFF==ord('d'):
    break

cv.waitKey(0)