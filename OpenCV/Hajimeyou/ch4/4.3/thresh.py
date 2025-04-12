import cv2
import numpy as np
import matplotlib.pyplot as plt

src_img = np.tile(np.arange(0,255,dtype=np.uint8), (256,1))
#np.tile(array, reps)

ret, th1 = cv2.threshold(src_img, 100, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(src_img, 100, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(src_img, 100, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(src_img, 100,255, cv2. THRESH_TOZERO)
ret, th5 = cv2.threshold(src_img, 100,255, cv2.THRESH_TOZERO_INV)
titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [src_img, th1, th2, th3, th4, th5]

plt.figure(figsize=(10,8))

for i , (title, img) in enumerate(zip(titles, images)):
    plt.subplot(2,3,i+1)
    plt.imshow(img, 'gray', vmin=0, vmax=255)
    plt.title(title)

plt.show()




