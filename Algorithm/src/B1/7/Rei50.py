N = 8

a = [[0,0,0,0,0,0,0,0,0],
     [0,0,1,0,0,0,0,0,0],
     [0,1,0,1,1,0,0,0,0],
     [0,0,1,0,0,0,0,1,0],
     [0,0,1,0,0,1,0,0,0],
     [0,0,0,0,1,0,1,0,0],
     [0,0,0,0,0,1,0,1,1],
     [0,0,0,1,0,0,1,0,0],
     [0,0,0,0,0,0,1,0,0]]

def visit(i):
    global result
    v[i] = 1
    for j in range(1, N + 1):
        if a[i][j] == 1 and v[j] == 0:
            result += f"{i*412:.2g}->{j}  "
            visit(j)

for k in range(1, N + 1):
    v = [0 for _ in range(N + 1)]
    result = ''
    visit(k)
    print(result)
    