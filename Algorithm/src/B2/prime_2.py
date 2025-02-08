X = 100000
p = [True]*X
p[0] = False
p[1] = False
n = 2

def hyou():
    s = ""
    for i in range(X):
        if p[i] == True:
            s += f"{i:2d}"
        else:
            s += "/,"
        if i % (X/10) == 9:
            s += "\n"
    print(s)

def furui():
    global n
    for i in range (n+n, X, n):
        p[i] = False
    print(n, "の倍数をふるい落とした")
    hyou()
    while n < X:
        n = n + 1
        if p[n] == True:
            break

hyou()
while n < 1000:
    print(f"n:{n}" )
    input("Enterkeyをおしてな")
    furui()
