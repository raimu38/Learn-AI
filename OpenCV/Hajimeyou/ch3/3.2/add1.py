import numpy as np
import cv2

x = np.array([250], dtype=np.uint8)
y = np.array([250], dtype=np.uint8)

z = cv2.add(x,y)
print(f"z = {z}")
