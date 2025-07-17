import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow("rectangle",rectangle)
cv.imshow("circle",circle)
          
#bitwise and
bw_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise_and", bw_and)     

#bitwise or
bw_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise_or", bw_or)

#bitwise xor
bw_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise_xor", bw_xor)

#bitwise not
bw_not = cv.bitwise_not(circle)
cv.imshow("not",bw_not)


cv.waitKey(0)