import cv2
import numpy as np

# ファイルパス
cfg     = 'yolov3.cfg'
weights = 'yolov3.weights'
names   = 'coco.names'

# クラス名リスト読み込み
with open(names) as f:
    CLASSES = [l.strip() for l in f]

# ネットワーク読み込み
net = cv2.dnn.readNetFromDarknet(cfg, weights)
# GPUを使いたい場合（CUDA対応版OpenCVが必要）
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

# 出力レイヤー名を直接取得（OpenCV 4.3+ 推奨）
out_layers = net.getUnconnectedOutLayersNames()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    h, w = frame.shape[:2]

    # 前処理：Blob化
    blob = cv2.dnn.blobFromImage(
        frame, 1/255.0, (416,416),
        swapRB=True, crop=False
    )
    net.setInput(blob)

    # 推論
    outs = net.forward(out_layers)

    boxes, confs = [], []
    for out in outs:
        for det in out:
            scores = det[5:]
            cid = np.argmax(scores)
            conf = scores[cid]
            if cid == 0 and conf > 0.5:  # person クラスID=0
                cx, cy, fw, fh = (det[0:4] * [w,h,w,h]).astype(int)
                x, y = cx - fw//2, cy - fh//2
                boxes.append([x,y,fw,fh])
                confs.append(float(conf))

    # NMS で重複除去
    idxs = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
    if len(idxs):
        for i in idxs.flatten():
            x,y,fw,fh = boxes[i]
            cv2.rectangle(frame, (x,y), (x+fw,y+fh), (255,0,0), 2)
            text = f"Person:{confs[i]:.2f}"
            cv2.putText(frame, text, (x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (255,0,0), 2)

    cv2.imshow('YOLOv3 Person', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
