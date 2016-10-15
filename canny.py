import cv2

img = cv2.imread('astana.jpg')

max_height = 500

if img.shape[0] > max_height:
    scale = (max_height * 1.0) / img.shape[0]
    img = cv2.resize(img, (0, 0), fx=scale, fy=scale)

edges = cv2.Canny(img, 100, 100)
a = edges[0:edges.shape[0], 0:edges.shape[1] / 2]

img[0:a.shape[0], 0:a.shape[1], 0] = a
img[0:a.shape[0], 0:a.shape[1], 1] = a
img[0:a.shape[0], 0:a.shape[1], 2] = a

cv2.imshow('test', img)
cv2.waitKey(0)
