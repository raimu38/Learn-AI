import cv2

img  = cv2.imread('neko1.jpg', cv2.IMREAD_COLOR)

zure = 500
print(img.shape[1])
src1 = img[:,:(img.shape[1] - zure)]
src2 = img[:,zure:]
alpha = 0.5
beta  = 0.5
gamma = 0.8

dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)

cv2.imshow("dsg", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


