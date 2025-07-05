import cv2, time, math, subprocess
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

last_action = 0
INTERVAL = 1.0

while True:
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)

    action_text = ""
    if res.multi_hand_landmarks:
        lm = res.multi_hand_landmarks[0].landmark
        h, w = frame.shape[:2]
        x1,y1 = int(lm[4].x*w), int(lm[4].y*h)
        x2,y2 = int(lm[8].x*w), int(lm[8].y*h)
        dist = math.hypot(x2-x1, y2-y1)

        cv2.line(frame, (x1,y1),(x2,y2),(0,255,0),2)
        cv2.circle(frame,(x1,y1),5,(0,0,255),-1)
        cv2.circle(frame,(x2,y2),5,(0,0,255),-1)

        now = time.time()
        if dist < 40 and now - last_action > INTERVAL:
            subprocess.run(['xdotool','key','Right'])
            action_text = "Next Slide"
            last_action = now
        elif dist > 120 and now - last_action > INTERVAL:
            subprocess.run(['xdotool','key','Left'])
            action_text = "Prev Slide"
            last_action = now

        mp_drawing.draw_landmarks(
            frame,
            res.multi_hand_landmarks[0],
            mp_hands.HAND_CONNECTIONS
        )

    if action_text:
        cv2.putText(frame, action_text, (30,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,255), 3)

    cv2.imshow("Gesture Control", frame)
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()

