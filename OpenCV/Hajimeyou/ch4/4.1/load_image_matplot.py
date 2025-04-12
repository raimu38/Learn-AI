import cv2
import matplotlib.pyplot as plt

img = cv2.imread('neko1.jpg', cv2.IMREAD_COLOR)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.imshow(img2)
plt.show()

