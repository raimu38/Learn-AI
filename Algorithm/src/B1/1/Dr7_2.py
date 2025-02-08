import math

N = 1000
prime = [1 for i in range(N + 1)]
limit = int(math.sqrt(N))
for i in range(2 , limit + 1):
    if prime[i] == 1:
        for j in range(2 * i, N + 1):
            if j % i == 0:
                prime[j] = 0