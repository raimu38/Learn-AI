import cv2
import mediapipe as mp
import numpy as np

mp_seg = mp.solutions.selfie_segmentation
seg = mp_seg.SelfieSegmentation(model_selection=1)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (640,480))
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = seg.process(rgb)

    mask = res.segmentation_mask > 0.5
    # 背景をグレーで用意
    bg = np.full(frame.shape, 128, dtype=np.uint8)
    output = np.where(mask[...,None], frame, bg)

    cv2.imshow('Selfie Segmentation', output)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
