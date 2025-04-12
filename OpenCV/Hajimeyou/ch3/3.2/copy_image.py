import numpy as np
import cv2

org_img = cv2.imread('neko1.jpg', cv2.IMREAD_COLOR)

mask = np.full((org_img.shape), 255, np.uint8)
cv_copy_img = cv2.copyTo(org_img, mask)

numpy_copy_img = np.copy(org_img)

shallow_copy_img = org_img

cv2.rectangle(org_img, (0,0), (100,100), (255,255,255), thickness=-1)

cv2.imshow("cv_copy_img", cv_copy_img)
cv2.imshow("numpy_copy_img", numpy_copy_img)
cv2.imshow("shallow_copy_img", shallow_copy_img)
cv2.imshow("org_img", org_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


