import numpy as np
import cv2

def is_same_image(src1, src2):
    diff = cv2.absdiff(src1, src2)
    print("diff:", diff)
    print("countNotZero:", cv2.countNonZero(diff))
    return (cv2.countNonZero(diff) == 0)


width = 200
height = 100

value1 = 128
value2 = 255

img1 = np.full((height, width), value1, np.uint8)
img2 = np.full((height, width), value2, np.uint8)


print(is_same_image(img1, img1))
print(is_same_image(img1, img2))

