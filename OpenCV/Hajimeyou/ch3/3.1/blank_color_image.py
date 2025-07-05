import numpy as np
import cv2


width = 200
height = 100
channels = 3
value = (0,0,255)


img1 = np.zeros((height, width), dtype=np.uint8)

img2 = np.full((height, width, channels), value, np.uint8)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
