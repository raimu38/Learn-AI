import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- 設定 ---
fs = 100  # サンプリング周波数 (Hz)
duration = 5  # 秒
t = np.linspace(0, duration, fs * duration, endpoint=False)

# --- 信号生成 ---
# 2Hz の正弦波を 0s～1s, 2s～3s, 4s～5s に出現させる
signal = np.zeros_like(t)
signal += np.where((t >= 0) & (t < 1), np.sin(2 * np.pi * 2 * t), 0)
signal += np.where((t >= 2) & (t < 3), np.sin(2 * np.pi * 2 * t), 0)
signal += np.where((t >= 4) & (t < 5), np.sin(2 * np.pi * 2 * t), 0)

# --- アニメーション準備 ---
fig, axs = plt.subplots(2, 1, figsize=(10, 6))
window_size = fs * 1  # 1秒のスライディングウィンドウ
step = int(fs * 0.1)  # 0.1秒ずつ移動

def animate(i):
    axs[0].cla()
    axs[1].cla()

    start = i * step
    end = start + window_size
    if end > len(t):
        return

    window_t = t[start:end]
    window_signal = signal[start:end]

    # FFT
    fft_result = np.fft.fft(window_signal)
    freqs = np.fft.fftfreq(window_size, d=1/fs)
    amplitude = np.abs(fft_result)

    # 時間領域プロット
    axs[0].plot(t, signal, color='lightgray', label='full signal')
    axs[0].plot(window_t, window_signal, color='blue', label='current window')
    axs[0].set_xlim(0, duration)
    axs[0].set_ylim(-1.2, 1.2)
    axs[0].set_title("Time Domain")
    axs[0].legend()

    # 周波数領域プロット（正の周波数のみ表示）
    axs[1].stem(freqs[:window_size // 2], amplitude[:window_size // 2], use_line_collection=True)
    axs[1].set_xlim(0, 10)
    axs[1].set_ylim(0, max(amplitude) * 1.1)
    axs[1].set_title("FFT Spectrum (Magnitude)")

ani = animation.FuncAnimation(fig, animate, frames=int((len(t) - window_size) / step), interval=100)
plt.tight_layout()
plt.show()

