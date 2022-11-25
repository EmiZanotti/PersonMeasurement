import math

import cv2 as cv
import numpy as np

img = cv.imread('5.jpg')


factor = 1
height, width, channels = img.shape
height = math.floor(height/factor)
width = math.floor(width/factor)
img = cv.resize(img, (width, height))



imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for c in contours:
    rect = cv.minAreaRect(c)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    cv.drawContours(img,[box],0,(0,0,255),2)

cv.imshow('frame',img)
while (True):
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()