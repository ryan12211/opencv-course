#pylint:disable=no-member

import cv2 as cv
import numpy as np

# Create a 500x500 black image with 3 color channels (BGR)
blank = np.zeros((500, 500, 3), dtype='uint8')

# Blue rectangle (BGR: 255, 0, 0)
rectangle = cv.rectangle(blank.copy(), (75, 75), (425, 425), (255, 0, 0), -1)

# Green circle (BGR: 0, 255, 0)
circle = cv.circle(blank.copy(), (250, 250), 175, (0, 255, 0), -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise operations
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

bitwise_not = cv.bitwise_not(circle)
cv.imshow('Circle NOT', bitwise_not)

cv.waitKey(0)
cv.destroyAllWindows()