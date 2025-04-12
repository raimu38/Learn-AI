import cv2

img = cv2.imread('neko1.jpg', cv2.IMREAD_COLOR)

img_roi = img[100:200, 300:500]

cv2.imshow("img", img)
cv2.imshow("img_roi", img_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

