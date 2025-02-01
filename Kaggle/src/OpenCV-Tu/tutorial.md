# OpenCV for Python: Getting Started Guide

このドキュメントでは、Python で OpenCV を使用するための基本的なコード例を紹介します。環境構築はすでに完了している前提で、実際にコードを書いて実行しながら、OpenCV の機能（画像の読み込み・表示、基本的な画像処理、描画、ビデオキャプチャ、フィルタ処理、エッジ検出、輪郭検出、顔検出など）を体系的に学んでいきます。

## 目次

1. [はじめに](#はじめに)
2. [基本的な画像入出力 (I/O)](#基本的な画像入出力-io)
3. [基本的な画像操作](#基本的な画像操作)
   - [リサイズ](#リサイズ)
   - [切り抜き](#切り抜き)
   - [カラースペースの変換](#カラースペースの変換)
4. [描画機能](#描画機能)
5. [ビデオキャプチャと処理](#ビデオキャプチャと処理)
6. [画像フィルタとエッジ検出](#画像フィルタとエッジ検出)
7. [輪郭検出](#輪郭検出)
8. [Haar カスケードを使った顔検出](#haarカスケードを使った顔検出)
9. [まとめと参考資料](#まとめと参考資料)

---

## はじめに

OpenCV (Open Source Computer Vision Library) は、画像処理やコンピュータビジョンの分野で広く使われているライブラリです。このガイドでは、Python を用いて OpenCV のさまざまな機能に触れていきます。各セクションに沿ってサンプルコードを実行しながら学習してください。

---

## 基本的な画像入出力 (I/O)

まずは画像をファイルから読み込み、ウィンドウに表示する方法を確認します。

```python
import cv2

# 画像を読み込む
image = cv2.imread('path_to_image.jpg')

# 画像が正しく読み込まれたか確認
if image is None:
    print("画像が見つかりません")
else:
    # 画像をウィンドウに表示
    cv2.imshow('Loaded Image', image)
    cv2.waitKey(0)  # キー入力待ち（無限に待つ）
    cv2.destroyAllWindows()  # 全ウィンドウを閉じる
```

### 説明

- `cv2.imread`: 指定したパスから画像を読み込みます。
- `cv2.imshow`: ウィンドウに画像を表示します。
- `cv2.waitKey(0)`: キー入力を無期限に待ちます。
- `cv2.destroyAllWindows()`: すべての OpenCV ウィンドウを閉じます。

---

## 基本的な画像操作

### リサイズ

画像のサイズを変更する例です。

```python
# 画像の50%にリサイズする例
scale_percent = 50  # 元画像の50%サイズ
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# 画像のリサイズ
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 切り抜き

画像の一部分を切り抜いて表示する例です。

```python
# 画像の一部を切り抜く (例: (50, 50)から100×100ピクセルの領域)
cropped = image[50:150, 50:150]
cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### カラースペースの変換

BGR 画像をグレースケールに変換する例です。

```python
# グレースケールに変換
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 描画機能

画像上に線、長方形、円、テキストなどを描画する方法です。描画には NumPy が必要となるので、先頭でインポートしてください。

```python
import cv2
import numpy as np

# 400×400の真っ白な画像（キャンバス）を作成
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
```

---

## ビデオキャプチャと処理

ウェブカメラまたはビデオファイルから動画を取得し、各フレームを処理・表示する例です。

```python
import cv2

# カメラ(デバイスインデックス0)からビデオキャプチャ
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("カメラを開けません")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("フレームの取得に失敗しました。終了します。")
        break

    # フレームをグレースケールに変換
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # フレームを表示
    cv2.imshow('Video - Press Q to exit', gray_frame)

    # 'q'キーが押されたらループ終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 画像フィルタとエッジ検出

### Gaussian Blur (ガウシアンブラー)

画像を平滑化してノイズを低減する例です。

```python
# ガウシアンブラーを適用
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow('Gaussian Blurred', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Canny エッジ検出

Canny アルゴリズムを用いて画像中のエッジを検出する例です。

```python
# Cannyエッジ検出を実施
edges = cv2.Canny(image, 100, 200)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 輪郭検出

画像内の輪郭を検出し、元画像に描画する例です。

```python
# グレースケールに変換し、二値化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 輪郭を検出
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 輪郭を元の画像に描画 (全輪郭を描画)
image_contours = image.copy()
cv2.drawContours(image_contours, contours, -1, (0, 255, 0), 3)

cv2.imshow('Contours', image_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## Haar カスケードを使った顔検出

OpenCV に用意されている Haar カスケード分類器を使って、画像内の顔を検出する方法です。

```python
# Haarカスケードファイルを読み込む
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 画像をグレースケールに変換（顔検出はグレースケール画像で行う）
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 顔を検出
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 検出された顔の領域に長方形を描画
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## まとめと参考資料

このガイドでは、Python と OpenCV を使った基本的な画像の読み込み、処理、描画、ビデオキャプチャ、フィルタ処理、輪郭検出、顔検出など、主要な機能を紹介しました。各サンプルコードを実際に動かしながら、OpenCV の機能を理解していってください。

### さらに学ぶための参考資料

- [OpenCV 公式ドキュメント](https://docs.opencv.org/)
- [PyImageSearch](https://www.pyimagesearch.com/)
- [OpenCV GitHub リポジトリ (Python サンプル)](https://github.com/opencv/opencv/tree/master/samples/python)

ぜひ、サンプルコードをカスタマイズしたり、組み合わせたりして、さまざまな画像処理の実装に挑戦してください。Happy Coding!
