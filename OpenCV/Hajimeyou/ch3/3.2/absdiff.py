import cv2

img1 = cv2.imread('neko1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('neko3.jpg', cv2.IMREAD_COLOR)

width = 1000
height = 800
src1 = img1[:height, :width]
src2 = img2[:height, :width]

diff = cv2.absdiff(src2, src1*8)
cv2.imshow('diff',diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
