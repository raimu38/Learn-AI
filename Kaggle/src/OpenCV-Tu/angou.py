import cv2
import numpy as np

x = 1
y = 2
z = 1

def transform_image(img):
    """偶数番目のピクセルを2倍にする（255超えは255にクリップ）"""
    transformed = img.copy()
    print(transformed)
    transformed[:len(transformed)-100:x, :len(transformed[0])-300:y] = np.clip(transformed[:len(transformed)-100:x, :len(transformed[0])-300:y] / z, 0, 255)
    # transformed[:, ::2] = transformed[::2,::2]*2
    return transformed

def restore_image(img):
    """偶数番目のピクセルを元に戻す（2で割る）"""
    restored = img.copy()
    restored[::x, ::y] = restored[::x, ::y] * z
    return restored

# 画像読み込み
image = cv2.imread("img/maxresdefault.jpg")

# 画像を変換
transformed_image = transform_image(image)

# 変換した画像を保存
cv2.imwrite("angou/transformed.jpg", transformed_image)

# 画像を復元
restored_image = restore_image(transformed_image)

# 復元した画像を保存
cv2.imwrite("angou/restored.jpg", restored_image)
