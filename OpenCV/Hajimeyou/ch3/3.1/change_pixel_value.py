import cv2

img = cv2.imread('neko1.jpg', cv2.IMREAD_COLOR)

x = 200
y = 100
channel = 0

print(f'before: bgr_val({x}, {y}) = {img[y,x]}')

img[y,x] = [255,255,255]

print(f'after: bgr_val({x}, {y}) = {img[y,x]}')

img[y,x,channel] = 0

print(f'after: bgr_val({x}, {y}) = {img[y,x,channel]}')



