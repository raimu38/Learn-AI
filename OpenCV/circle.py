import cv2
import numpy as np

# 1) Open the first camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 2) Blur and convert to HSV color space
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # 3) Define red color range in HSV
    #    You can tweak these lower/upper bounds for your object
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red2 = np.array([170,120,70])
    upper_red2 = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # 4) Clean up the mask
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # 5) Find contours and pick the largest
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    center = None
    if contours:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        if M["m00"] > 0:
            center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))

            # 6) Draw circle and centroid if object is large enough
            if radius > 10:
                cv2.circle(frame, (int(x),int(y)), int(radius), (0,255,0), 2)
                cv2.circle(frame, center, 5, (0,0,255), -1)
                cv2.putText(frame, "Red Ball", (center[0]-20, center[1]-20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    # 7) Show result
    cv2.imshow("Color Tracking", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()

