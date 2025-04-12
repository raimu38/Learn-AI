import cv2

img = cv2.imread("neko1.jpg", cv2.IMREAD_COLOR)

timer = cv2.TickMeter() #Timer呼び出し

timer.start()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

timer.stop()

mesurement_timer = timer.getTimeMilli()
print(f"経過時間: {mesurement_timer:.2f}")

