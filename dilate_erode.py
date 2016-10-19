import cv2
import numpy as np

img = cv2.imread('astana.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
img2 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
d = cv2.dilate(img2, kernel)
e = cv2.erode(img2, kernel)
cv2.imshow('dilate', d)
cv2.imshow('erode', e)
cv2.waitKey(0)
