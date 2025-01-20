# 必要ライブラリインポート
import qiskit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt  # 追加
from qiskit import ClassicalRegister, QuantumRegister
from qiskit import QuantumCircuit

# シミュレータの設定
backend_sim = AerSimulator()

# 量子レジスタと古典レジスタを設定
q = QuantumRegister(4)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

# 0、1番目の量子ビットにXゲートを配置
qc.x(q[0])
qc.x(q[1])

# その他のゲートにCXゲートを配置
qc.ccx(q[0], q[1], q[2])
qc.cx(q[0], q[3])
qc.cx(q[1], q[3])

# 測定
qc.measure(q[2], c[1])
qc.measure(q[3], c[0])

# シミュレーションの実行
job_1 = backend_sim.run(qc)

# 結果を取得
result = job_1.result()
counts = result.get_counts(qc)

# ヒストグラムをプロット
hist = plot_histogram(counts)

# 結果をPNGとして保存
hist.savefig("quantum_result.png")  # 保存ファイル名を指定

# 表示 (オプション)
plt.show()
