import cv2
import numpy as np

img = cv2.imread("neko1.jpg", cv2.IMREAD_COLOR)

b_plane, g_plane, r_plane = cv2.split(img)
b_plane  = cv2.merge([b_plane, np.zeros_like(b_plane), np.zeros_like(b_plane)])


print("b_plane", b_plane)
cv2.imshow("b_plane", b_plane)
cv2.imshow("g_plane", g_plane)
cv2.imshow("r_plane", r_plane)

cv2.waitKey(0)
cv2.destroyAllWindows()
