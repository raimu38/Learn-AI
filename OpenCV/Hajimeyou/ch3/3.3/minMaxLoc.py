import numpy as np
import cv2

img = np.array([[1,2,3],[4,5,6]])

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img)

print(f"min_val:{min_val}")
print(f"max_val:{max_val}")
print(f"min_loc:{min_loc}")
print(f"max_loc:{max_loc}")
