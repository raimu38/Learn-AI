import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

file1 = 'drive.jpg'
if  not os.path.isfile(file1):
    raise FileNotFoundError('Image not found')

img1 = cv2.imread('drive.jpg')
img = cv2.imread('drivecam.jpg')

src_pts = np.array([(670,680),(1130,680),(130,800),(1600,800)], dtype=np.float32)
dst_pts = np.array([(0,0), (500,0),(0,500),(500,500)], dtype=np.float32)

M = cv2.getPerspectiveTransform(src_pts, dst_pts)
print(M)
dst_img = cv2.warpPerspective(img, M, (500,500))

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
plt.imshow(cv2.cvtColor(dst_img, cv2.COLOR_BGR2RGB))
plt.show()
