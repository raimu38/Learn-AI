import random

N = 10
a = [0 for i in range(N)]
a[0] = random.randint(1,N)

for i in range(1, N):
    while True:
        a[i] = random.randint(1,N)
        flag = 0
        for j in range(i):
            if a[i] == a[j]:
                flag = 1
                break
        if flag == 0:
            break
print(a)

