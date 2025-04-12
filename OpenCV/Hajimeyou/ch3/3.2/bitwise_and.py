import numpy as np
import cv2

src1 = cv2.imread("neko1.jpg", cv2.IMREAD_COLOR)

heigth , width , channels = src1.shape[:3]

src2 = np.zeros((heigth,width,channels), np.uint8)
cv2.rectangle(src2, (0, 0), (width-200, heigth),(255,0,0), thickness=500)

dst = cv2.bitwise_or(src1, src2)

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

