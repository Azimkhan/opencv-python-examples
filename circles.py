import cv2
import numpy as np
image = cv2.imread('balls.jpg')

output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 100,
              param1=250,
              param2=50,
              minRadius=10,
              maxRadius=100)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(output,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(output,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow("image", output)

cv2.waitKey(0)
