import random

N = 10000000
a = 0

for i in range(N):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        a += 1

pi = 4*a/N
print(f"円周率は{pi:5.9}")