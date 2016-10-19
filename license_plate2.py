import cv2
import numpy as np
import pytesseract
from PIL import Image

img = cv2.imread('plate2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)

cv2.imshow('img2', thresh)
all_contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

LENGTH = len(all_contours)
char_pieces = []
for i in range(LENGTH):
    cnt = all_contours[i]
    x, y, w, h = cv2.boundingRect(cnt)
    if 12 < h < 70 and 10 < w < 50:
        ratio = h * 1.0 / w
        # print ratio
        var = hierarchy[0][i]

        if 2.2 > ratio > 0.99:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            char_pieces.append((x, y, w, h))

x
def cmp2(o1, o2):
    if o1[0] > o2[0]:
        return 1
    elif o1[0] < o2[0]:
        return -1
    else:
        return 0


def detect_plate_text(char_p):
    chars = []
    prev = None
    for rect in char_p:
        # print rect
        x, y, w, h = rect
        if prev is not None and x - prev[0] > 50:
            chars = []
        prev = rect
        char = thresh[y:y + h, x:x + w, ]
        # cv2.imshow(str(rect), char)
        c = pytesseract.image_to_string(Image.fromarray(char), config='-psm 10')
        chars.append(c)
        if len(chars) == 10:
            text = ''.join(chars).lower()
            if text.startswith('kz'):
                return text
            else:
                chars = []


char_pieces.sort(cmp=cmp2)
plate_text = detect_plate_text(char_pieces)
if plate_text:
    cv2.putText(img, plate_text, (20, 20), cv2.FONT_HERSHEY_PLAIN, 1, 0xffffff, 1, cv2.CV_AA)

cv2.imshow('img3', thresh)

cv2.imshow('img', img)
cv2.waitKey(0)
