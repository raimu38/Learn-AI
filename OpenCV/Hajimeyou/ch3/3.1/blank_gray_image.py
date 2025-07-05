import numpy as np
import cv2

WIDTH = 200
HEIGHT = 100
VALUE = 128 

img1 = np.zeros((HEIGHT, WIDTH ), np.uint8)

print(f"img1: {img1}")


img2 = np.full((HEIGHT, WIDTH), VALUE, np.uint8)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

