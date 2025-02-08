a = [43,65,23,7,5,74,76,43,100,89,87,97,25]
N = len(a)
juni = [0 for i in range(N)]

for i in range(N):
    juni[i] = 1
    for j in range(N):
        if a[i] < a[j]:
            juni[i] += 1

print('得点',' 順位')
for i in range(N):
    print('{:3d} {:3d} 位'.format(a[i],juni[i]))
