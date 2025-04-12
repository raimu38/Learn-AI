import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("/home/kougami/Downloads/chocolates.jpg")
if img is None:
    print("Error: Could not open or find the image.")
    exit()

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(img_hsv)

plt.figure(figsize=(15,10))

plt.subplot(2, 3, 1)
plt.title("Original(RGB)")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(2, 3, 2)
plt.title("Hue")
plt.imshow(h, cmap='hsv')

plt.subplot(2, 3, 3)
plt.title("Saturation")
plt.imshow(s, cmap='gray')

plt.subplot(2, 3, 4)
plt.title("Value")
plt.imshow(v, cmap='gray')

# mask を NumPy配列として初期化 (グレースケール画像と同じ形状とデータ型)
mask = np.zeros_like(h)

# NumPyの条件インデックスを使用して、条件を満たす要素に 255 を代入
mask[(h > 80) & (h < 140) & (s > 50)] = 255

mask_3ch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
result_img = cv2.bitwise_or(img, mask_3ch)
cv2.imshow('Result', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
