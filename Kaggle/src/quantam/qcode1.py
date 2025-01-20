# 必要ライブラリインポート
from qiskit import QuantumCircuit
from qiskit.primitives import Sampler
import matplotlib.pyplot as plt

sampler = Sampler() 

# QuantumCircuitオブジェクト作成。(1,1)は1つの量子ビットと1つの古典ビットを持つ。
qc = QuantumCircuit(1, 1)
# Hゲートを配置
qc.h(0)
# 測定
qc.measure([0], [0])

# 配置した量子回路を実行する
job = sampler.run(qc)

# 回路の実行結果を取得
result = job.result()

# 結果を表示
print(f">>> {result}")
print(f"  > Quasi-distribution: {result.quasi_dists[0]}")

# 量子回路を作図し、画像として保存
qc.draw('mpl')
plt.savefig('quantum_circuit.png')  # 量子回路を画像に保存

# 結果の確率分布を保存
with open('result.txt', 'w') as f:
    f.write(f"Quasi-distribution: {result.quasi_dists[0]}\n")
