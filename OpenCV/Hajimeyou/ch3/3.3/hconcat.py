import cv2 

img1 = cv2.imread("neko1.jpg", cv2.IMREAD_COLOR)
img2 = cv2.flip(img1, 0) 

hconcat_img = cv2.hconcat([img1, img2])

cv2.imshow("hconcat_img", hconcat_img)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
