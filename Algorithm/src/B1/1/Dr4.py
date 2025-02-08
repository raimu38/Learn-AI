import random

N = 100
a = [i + 1 for i in range(N)]

for i in range(N-1, 0, -1):
    j = random.randint(0, i - 1)
    a[i], a[j] = a[j], a[i]

print(a)

