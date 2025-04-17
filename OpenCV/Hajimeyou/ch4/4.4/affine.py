import cv2
import numpy as np
from matplotlib import pyplot as plt

width , height = 100, 100
src_img = np.full((height, width, 3), 128, dtype=np.uint8)
cv2.rectangle(src_img, (10,10), (width - 10, height -30), (255,255,0), -1)
cv2.rectangle(src_img, (30,40), (35,45), (255,0,0), -1)
cv2.putText(src_img, 'AI', (30,40), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,255,0), 1, cv2.LINE_4)

plt.imshow(src_img, 'gray')
plt.show()

x = 50
y = -10
M_shift = [[1,0,x],
           [0,1,y]]

M_shift = np.array(M_shift, dtype=np.float32)
sheer_img = cv2.warpAffine(src_img, M_shift, dsize=(width, height))
plt.imshow(sheer_img, 'gray')
plt.show()


angle = 45
M_rotate = cv2.getRotationMatrix2D(center=(0, 0), angle=angle, scale=2.0)
rotating_img = cv2.warpAffine(src_img, M_rotate, dsize=(width*3, height*3))
plt.imshow(rotating_img, 'gray')
plt.show()

a = 0.2
b = 0.0
M_shear = [[1,a,0],
           [b,1,0]]
M_shear = np.array(M_shear, dtype=np.float32)
shear_img = cv2.warpAffine(src_img, M_shear, dsize=(width*2, height*3))
plt.imshow(shear_img, 'gray')
plt.show()
