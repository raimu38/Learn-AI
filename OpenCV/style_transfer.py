# style_transfer.py
import cv2, os

model_path = 'models/mosaic.t7'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"{model_path} が見つかりません")

net = cv2.dnn.readNetFromTorch(model_path)
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret: break
    blob = cv2.dnn.blobFromImage(
        frame, 1.0, (512,512),
        (103.939,116.779,123.68),
        swapRB=False, crop=True
    )
    net.setInput(blob)
    out = net.forward().squeeze().transpose(1,2,0)
    out += (103.939,116.779,123.68)
    out = cv2.resize(out, (frame.shape[1], frame.shape[0]))
    out = cv2.convertScaleAbs(out)
    cv2.imshow('Style Transfer', out)
    if cv2.waitKey(1)&0xFF==27: break
cap.release()
cv2.destroyAllWindows()

