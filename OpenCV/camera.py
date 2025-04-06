
import cv2

# モデルファイル（事前にダウンロード）
prototxt = 'MobileNetSSD_deploy.prototxt'
model    = 'MobileNetSSD_deploy.caffemodel'

# クラス名リスト（person は index 15）
CLASSES = ["background", "aeroplane","bicycle","bird","boat",
           "bottle","bus","car","cat","chair","cow","diningtable",
           "dog","horse","motorbike","person","pottedplant",
           "sheep","sofa","train","tvmonitor"]

net = cv2.dnn.readNetFromCaffe(prototxt, model)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300,300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    (h, w) = frame.shape[:2]
    for i in range(detections.shape[2]):
        confidence = detections[0,0,i,2]
        idx = int(detections[0,0,i,1])
        if CLASSES[idx] == "person" and confidence > 0.5:
            box = detections[0,0,i,3:7] * [w,h,w,h]
            x1,y1,x2,y2 = box.astype("int")
            cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 2)
            cv2.putText(frame, f"Person: {confidence:.2f}",
                        (x1,y1-10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (255,0,0), 2)

    cv2.imshow('SSD Person Detector', frame)
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
