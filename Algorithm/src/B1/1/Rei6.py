m, n = 1203958*567,1203958*67893 

while  m != n:
    if m > n :
        m -= n
    else:
        n -= m
print(f"最大公約数は{m:d}")

m,n = 21, 35
while True:
    k = m % n
    m = n
    n = k
    if k == 0:
        break
print(f'最大公約数は{m}')