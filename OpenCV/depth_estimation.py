import cv2
import numpy as np
import os

model_path = 'models/midas_v21_small_256.onnx'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"{model_path} が見つかりません")

net = cv2.dnn.readNet(model_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    h, w = frame.shape[:2]

    # 前処理：リサイズ→BGR→RGB→Blob
    inp = cv2.resize(frame, (256,256))
    blob = cv2.dnn.blobFromImage(
        inp, 1/255.0, (256,256),
        mean=(0.485,0.456,0.406),
        swapRB=True, crop=False
    )
    net.setInput(blob)
    depth = net.forward()[0,0,:,:]

    # 可視化用に正規化→カラーマップ
    depth = cv2.resize(depth, (w,h))
    dmin, dmax = depth.min(), depth.max()
    disp = ((depth-dmin)/(dmax-dmin)*255).astype(np.uint8)
    disp_color = cv2.applyColorMap(disp, cv2.COLORMAP_INFERNO)

    # 左:元映像 右:深度マップ
    vis = np.hstack([frame, disp_color])

    cv2.imshow('MiDaS Depth', vis)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

