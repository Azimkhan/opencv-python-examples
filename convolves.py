import cv2
import numpy as np

kernel = np.ndarray(shape=(3, 3), dtype=float)
kernel.fill(0.1)
img = cv2.imread('astana.jpg')

max_height = 500

if img.shape[0] > max_height:
    scale = (max_height * 1.0) / img.shape[0]
    img = cv2.resize(img, (0, 0), fx=scale, fy=scale)

img2 = cv2.filter2D(img, -1, kernel)
cv2.imshow('mod', img2)
cv2.imshow('original', img)
cv2.waitKey(0)
