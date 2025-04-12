import cv2

img = cv2.imread('vegetable.png')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


h, s, v = cv2.split(hsv_img)

cv2.imshow('H, S, V', cv2.hconcat([h,s,v]))

cv2.waitKey(0)
cv2.destroyAllWindows()
