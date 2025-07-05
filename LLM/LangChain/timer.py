# timer.py
import time
import sys
import json

def run_timer(seconds):
    print(f"⏳ タイマー開始: {seconds}秒")
    time.sleep(seconds)
    print("🔔 タイマー終了！")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使い方: python timer.py '{\"seconds\": 10}'")
        sys.exit(1)
    try:
        cmd = json.loads(sys.argv[1])
        seconds = cmd.get("seconds", 60)
        run_timer(seconds)
    except Exception as e:
        print(f"エラー: {e}")
