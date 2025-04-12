import cv2

img = cv2.imread("neko1.jpg", cv2.IMREAD_COLOR)

rotate_flags = [
        None, cv2.ROTATE_90_CLOCKWISE, cv2.ROTATE_180, cv2.ROTATE_90_COUNTERCLOCKWISE
]

for i in range(4):
    if rotate_flags[i] is None:
        rorated = img
    else:
        rorated = cv2.rotate(img, rotate_flags[i])

    cv2.imshow(f"rorated_{i*90}", rorated)

cv2.waitKey(0)
cv2.destroyAllWindows()
