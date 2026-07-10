#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/miels.jpg')
cv.imshow('Original', img)

# Convert BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Split HSV channels
h, s, v = cv.split(hsv)

# Change the Hue (color)
# Add 50 to the hue (values wrap around at 180)
h = (h.astype(np.int16) + 50) % 180
h = h.astype(np.uint8)

# Merge the channels
new_hsv = cv.merge([h, s, v])

# Convert back to BGR for display
new_bgr = cv.cvtColor(new_hsv, cv.COLOR_HSV2BGR)

cv.imshow('Changed Color', new_bgr)

cv.waitKey(0)
cv.destroyAllWindows()