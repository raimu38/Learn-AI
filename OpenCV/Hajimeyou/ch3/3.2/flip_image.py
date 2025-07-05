import cv2

src = cv2.imread("neko1.jpg", cv2.IMREAD_COLOR)

dstX = cv2.flip(src, 0)
dstY = cv2.flip(src, 1)
dstXY  = cv2.flip(src, -1)

cv2.imshow("src", src)
cv2.imshow("dstX", dstX)
cv2.imshow("dstY", dstY)
cv2.imshow("dstXY", dstXY)

cv2.waitKey(0)
cv2.destroyAllWindows()
