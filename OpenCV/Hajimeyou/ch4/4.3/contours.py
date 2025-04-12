import cv2
import matplotlib.pyplot as plt

img_bgr = cv2.imread('bolts.jpg')
img_bgr = cv2.resize(img_bgr, (500,375))
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)


ret, img_bin = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours = list(filter(lambda x:cv2.contourArea(x) > 10, contours))


result_img = cv2.drawContours(img_bgr.copy(), contours, -1, (0,155,100), 1)

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    result_img = cv2.rectangle(result_img, (x,y), (x+w, y+h), (255,0,0,), 4)

titles = ['Input Image', 'Grayscale', 'cv2.threshold', 'result']
images = [img_bgr, img_gray, img_bin, result_img]

fig = plt.figure(figsize=(24,6))

for index, (title, image) in enumerate(zip(titles, images)):
    ax = fig.add_subplot(1, len(images), index + 1)
    ax.set_title(title)
    ax.imshow(image, 'gray')
    ax.axis('on')

plt.show()
