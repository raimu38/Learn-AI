import numpy as np
import cv2

img = cv2.imread('neko1.jpg', cv2.IMREAD_COLOR)


x = 200
y = 100
channel = 0


print("img.shape:", img.shape)
bar_val = img[y,x]
print(f"bgr_val({x}, {y}) = {bar_val}")

b_val = img[y, x, channel]
print(f"b_val({x}, {y}) = {b_val}")



