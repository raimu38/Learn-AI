import numpy as np
import time

# NumPy配列の例
a = np.arange(100)
# print(a)
start = time.time()
b = a * 2
end = time.time()
print(f"NumPy配列の処理時間: {end - start}秒")


import time

# Pythonリストの例
a = list(range(100))
start = time.time()
b = [x * 2 for x in a]
end = time.time()
print(f"Pythonリストの処理時間: {end - start} 秒")

# ネイピア数
import numpy as np
print(np.e)
print(np.exp(2))

print(np.log(np.e))
print(np.log(np.exp(2)))
