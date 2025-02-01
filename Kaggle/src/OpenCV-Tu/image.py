import cv2
import numpy as np 

image = cv2.imread('./img/maxresdefault.jpg')
if image is None:
    print("画像が見つかりません")
else:
    width = image.shape[1]

scale_percent = 50
height , width = [int(dim * 50 /100 ) for dim in image.shape[:2]]
dim = (width, height)
resized = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("Resized Image",resized)

cropped = image[50:150, 50:100]
cv2.imshow('CroppedImage',cropped)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Graysclae Image',gray)

canvas = 255 * np.ones((400,400,))# 400×400の真っ白な画像（キャンバス）を作成
canvas = 255 * np.ones((400, 400, 3), dtype=np.uint8)

# 青い線を描く (始点 (50, 50) から終点 (350, 50))
cv2.line(canvas, (50, 50), (350, 50), (255, 0, 0), thickness=5)

# 緑色の長方形を描く (左上 (50, 100), 右下 (350, 300))
cv2.rectangle(canvas, (50, 100), (350, 300), (0, 255, 0), thickness=3)

# 赤色の円を描く (中心 (200, 350), 半径 40, 塗りつぶし)
cv2.circle(canvas, (200, 350), 40, (0, 0, 255), thickness=-1)

# 画像上にテキストを描画
cv2.putText(canvas, 'OpenCV Demo', (70, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.imshow('Drawing', canvas)












cv2.waitKey(0)
cv2.destroyAllWindows()




