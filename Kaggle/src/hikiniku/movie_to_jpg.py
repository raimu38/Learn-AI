import cv2
import os

def extract_frames(video_path, output_dir, start_time, end_time, interval=5, fps=30):
    """
    動画からフレームを抽出し画像として保存する。
    
    Parameters:
        video_path (str): 動画ファイルのパス
        output_dir (str): 抽出した画像を保存するディレクトリ
        start_time (int): 開始秒
        end_time (int): 終了秒
        interval (int): 何フレームごとに保存するか
        fps (int): 動画のフレームレート
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: 動画を開けませんでした")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    video_fps = int(cap.get(cv2.CAP_PROP_FPS))
    print(f"動画の総フレーム数: {total_frames}, FPS: {video_fps}")

    # 開始フレームと終了フレームを計算
    start_frame = int(start_time * video_fps)
    end_frame = int(end_time * video_fps)

    current_frame = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 指定した範囲のフレームのみ処理
        if start_frame <= current_frame <= end_frame:
            # 指定した間隔でフレームを保存
            if (current_frame - start_frame) % (interval * fps) == 0:
                output_file = os.path.join(output_dir, f"frame_{saved_count:04d}.jpg")
                cv2.imwrite(output_file, frame)
                print(f"Saved: {output_file}")
                saved_count += 1

        current_frame += 1
        if current_frame > end_frame:
            break

    cap.release()
    print(f"フレーム抽出完了: {saved_count}枚保存しました。")

# 実行例
video_file = "beef.MOV"  # 動画ファイルパス
output_folder = "beef/pork"  # 保存ディレクトリ
extract_frames(video_file, output_folder, start_time=1, end_time=20, interval=4, fps=1)





