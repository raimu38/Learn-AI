# aruco_distance_fixed.py
import cv2
import numpy as np

# 1) ArUco 辞書と検出器
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
params     = cv2.aruco.DetectorParameters()
detector   = cv2.aruco.ArucoDetector(aruco_dict, params)

# 2) カメラ内部パラメータ（要キャリブレーション）
fx = fy = 800.0
cx = 320.0
cy = 240.0
camera_matrix = np.array([[fx,  0, cx],
                          [ 0, fy, cy],
                          [ 0,  0,  1]])
dist_coeffs = np.zeros((5,1))

# 3) マーカー実サイズ（m単位）
marker_length = 0.05  # 5cm

# 4) マーカーの 3D 座標（マーカー中心を原点に）
#    順序は検出時の corners[0] の順序に合わせる
half = marker_length / 2
object_pts = np.array([
    [-half,  half, 0],
    [ half,  half, 0],
    [ half, -half, 0],
    [-half, -half, 0],
], dtype=np.float32)

# 5) カメラ起動
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = detector.detectMarkers(gray)

    if ids is not None:
        # 検出マーカーを囲む四角を描画
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        for corner in corners:
            img_pts = corner[0].astype(np.float32)  # shape (4,2)

            # 6) solvePnP で姿勢推定
            success, rvec, tvec = cv2.solvePnP(
                object_pts,
                img_pts,
                camera_matrix,
                dist_coeffs,
                flags=cv2.SOLVEPNP_ITERATIVE
            )
            if not success:
                continue

            # 距離（m）を計算
            dist = np.linalg.norm(tvec)

            # 7) 座標軸を描画（長さ marker_length の半分）
            cv2.drawFrameAxes(
                frame, camera_matrix, dist_coeffs,
                rvec, tvec, marker_length/2, 2
            )

            # マーカー左上角に距離テキスト表示
            pt = tuple(img_pts[0].astype(int))
            cv2.putText(frame,
                        f"{dist*100:.1f} cm",
                        pt,
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0,255,0),
                        2)

    cv2.imshow('ArUco Distance (fixed)', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

