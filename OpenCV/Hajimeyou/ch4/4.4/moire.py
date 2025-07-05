import cv2
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,16,3000)
y = np.linspace(0,16,3000)

xx, yy = np.meshgrid(x,y)
x = np.linspace(0, 1, 100)
y = np.linspace(1, 0, 100)
xx, yy = np.meshgrid(x, y)

r = np.sqrt(xx**2 + yy**2)  # 中心からの距離
print(r)
plt.imshow(r, cmap='plasma')
plt.show()

