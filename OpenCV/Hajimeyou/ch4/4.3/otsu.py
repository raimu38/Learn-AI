import cv2
import numpy as np
import matplotlib.pyplot as plt

src_img = np.full((100,500,3), 255, dtype=np.uint8)

v = (50,200)

colors = [(b, g, r) for r in v for g in v for b in v]

for i , color in enumerate(colors):
    cv2.circle(src_img, (i*60+40, 50), 30, color, -1)

gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

ret, img_otsu = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("大津のしきい値 : ", ret)

ret, img_triangle = cv2.threshold(gray_img, 127,255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)
print("トライアングルのしきい値:", ret)

titles  = ['Originla', 'Gray', 'THRESH_OTSU', 'TRESH_TRIANGLE']
images  = [src_img, gray_img, img_otsu, img_triangle]
gohans  = ['kome', 'miso','sio', 'tukemono']

zipped = list(zip(titles, gohans))

for i, title_images in enumerate(zip(titles, images)):
    title, image = title_images
    plt.subplot(4,1,i + 1)
    plt.title(title)
    plt.imshow(image, 'gray', vmin=0, vmax=255)

plt.show()

