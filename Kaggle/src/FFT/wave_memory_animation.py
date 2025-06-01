"""
wave_memory_animation.py

波動的記憶モデルのアニメーション出力プロトタイプ
-------------------------------------------------
- 内部波動(state)が入力（波）を受け取るたびに干渉・変化し、減衰していく様子を
  アニメーションとして描画して MP4 で保存する
- 各入力波は「指定されたフレーム」で一度に加算され、その後は減衰のみ行う
- フレームごとに内部状態をプロットし、学習・記憶の流れを可視化する
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ----------------------------------------
# 設定
# ----------------------------------------
FS = 100               # サンプリング周波数（Hz）, 擬似的に使うだけ
MEMORY_LENGTH = 500    # 内部波動を表すベクトル長
DECAY_RATE = 0.98      # 1フレームごとに適用する減衰率

# 入力波の準備
def generate_sine_wave(freq, phase=0.0, length=MEMORY_LENGTH, fs=FS):
    """
    freq: 周波数 (Hz)
    phase: 初期位相 (rad)
    length: サンプル数
    fs: サンプリング周波数
    """
    t = np.arange(length) / fs
    return np.sin(2 * np.pi * freq * t + phase)

# ----------------------------------------
# 波動的記憶モデルクラス
# ----------------------------------------
class WaveMemory:
    def __init__(self, length=MEMORY_LENGTH, decay=DECAY_RATE):
        self.length = length
        self.decay = decay
        self.state = np.zeros(length, dtype=np.float32)

    def add_input_wave(self, wave):
        """
        入力波を内部波に重ね合わせる。減衰は別途 call_decay() で実行する。
        """
        self.state += wave

    def call_decay(self):
        """
        減衰のみを行う
        """
        self.state *= self.decay

    def get_state(self):
        """
        現在の内部波動を返す（正規化なし）
        """
        return self.state

# ----------------------------------------
# アニメーション用セットアップ
# ----------------------------------------
# 各入力波を作成
wave_A = generate_sine_wave(freq=2.0, phase=0.0)       # 2Hz
wave_B = generate_sine_wave(freq=5.0, phase=np.pi/4)   # 5Hz
wave_C = generate_sine_wave(freq=7.0, phase=np.pi/2)   # 7Hz

# 仮説波 D (A + B)
hypothesis_D_raw = wave_A + wave_B
hypothesis_D = hypothesis_D_raw / np.linalg.norm(hypothesis_D_raw) if np.linalg.norm(hypothesis_D_raw) > 0 else hypothesis_D_raw

# 創造波 E (D + 8Hz)
wave_E = generate_sine_wave(freq=8.0, phase=np.pi/3)
creative_E_raw = hypothesis_D + 0.5 * wave_E
creative_E = creative_E_raw / np.linalg.norm(creative_E_raw) if np.linalg.norm(creative_E_raw) > 0 else creative_E_raw

# アニメーション設定
PHASES = [("Wave A", wave_A), ("Wave B", wave_B), ("Wave C", wave_C), ("Creative E", creative_E)]
FRAMES_PER_PHASE = 30    # 各波を加算してから減衰させるフレーム数
TOTAL_PHASES = len(PHASES)
TOTAL_FRAMES = TOTAL_PHASES * FRAMES_PER_PHASE

wm = WaveMemory()

fig, ax = plt.subplots(figsize=(6, 3))
line, = ax.plot([], [], color='navy')
ax.set_ylim(-4, 4)
ax.set_xlim(0, MEMORY_LENGTH - 1)
ax.set_xlabel("Sample Index")
ax.set_ylabel("Amplitude")
title_text = ax.set_title("")

# ----------------------------------------
# アニメーション関数
# ----------------------------------------
def init():
    line.set_data([], [])
    title_text.set_text("")
    return line, title_text

def animate(frame_idx):
    # どのフェーズか判定
    phase_idx = frame_idx // FRAMES_PER_PHASE
    local_idx = frame_idx % FRAMES_PER_PHASE

    # フェーズ開始時（local_idx == 0）に波を一度だけ加算
    if local_idx == 0:
        _, wave = PHASES[phase_idx]
        wm.add_input_wave(wave)

    # 減衰は毎フレーム実行
    wm.call_decay()

    # プロット更新
    current_state = wm.get_state()
    line.set_data(np.arange(MEMORY_LENGTH), current_state)
    phase_name, _ = PHASES[phase_idx]
    title_text.set_text(f"Phase: {phase_name} (Frame {frame_idx + 1}/{TOTAL_FRAMES})")
    return line, title_text

# ----------------------------------------
# アニメーション作成および保存
# ----------------------------------------
ani = animation.FuncAnimation(
    fig, animate, frames=TOTAL_FRAMES, init_func=init,
    interval=100, blit=True
)

# MP4 形式で保存 (ffmpeg が必要)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=10, metadata=dict(artist='WaveMemory'), bitrate=1800)
ani.save("wave_memory_demo.mp4", writer=writer)

print("MP4ファイル (wave_memory_demo.mp4) を出力しました。")

