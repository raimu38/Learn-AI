import cv2

img = cv2.imread('neko1.jpg', cv2.IMREAD_COLOR)

if (len(img.shape) == 3):
    height , width , channels = img.shape
else:
    height, width = img.shape
    channels = 1

print(f"width: {width}")

print(f"height: {height}")

print(f"channels: {channels}")

print(img.shape[:2])

