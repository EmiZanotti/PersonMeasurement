# import the necessary packages
import numpy as np
import cv2
import math
 
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()


# Read image
frame = cv2.imread('2.jpg')

# Calculo dimensiones imagen\

factor = 4
height, width, channels = frame.shape
height = math.floor(height/factor)
width = math.floor(width/factor)
frame = cv2.resize(frame, (width, height))


# using a greyscale picture, also for faster detection
gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

# detect people in the image
# returns the bounding boxes for the detected objects
boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )

boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

for (xA, yA, xB, yB) in boxes:
    # display the detected boxes in the colour picture
    cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
    print(xA, xB, yA, yB)


cv2.imshow('frame',frame)
while (True):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)