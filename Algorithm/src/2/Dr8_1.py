def irnd():
    global rndnum
    rndnum = (rndnum*109 + 1021) % 32768
    return rndnum

def rnd():
    return irnd() / 32767.1

N = 1000
M = 10
F = N / M 
SCALE = 40.0

rndnum = 13
hist = [0 for i in range(M + 1)]
e = 0.0

for i in range(N):
    rank = int(M*rnd() + 1)
    hist[rank] += 1

for i in range(1, M + 1):
    result = '{:3d}:{:3d}'.format(i, hist[i])
    result += '*' * int(hist[i] * SCALE)
    print(result)
    e += (hist[i] - F) * (hist[i] - F)/F

print('カイ2乗={:f}'.format(e))