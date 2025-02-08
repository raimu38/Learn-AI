a = [43,65,23,7,5,74,76,43,100,89,87,97,25]
Max = 100
Min = 0

juni = [0 for i in range(Max + 2)]
N = len(a)
for i in range(N):
    juni[a[i]] += 1

juni[Max + 1] = 1
for i in range(Max, Min - 1, -1):
    juni[i] += juni[i + 1]

print('得点　順位')
for i in range(N):
    print(('{:6d}{:6d}'.format(a[i],juni[a[i] + 1])))