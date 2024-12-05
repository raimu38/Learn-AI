# N = 100

# numbers = [i + 1 for i in range(2 * N)]
# sosu = [2];
# for i in range(2, 2 * N):
#     while True:
#         count = 1
#         if numbers[count] % i == 0:
#             sosu.append(i)
#             numbers.remove(i)

import math
            
while( data := input('data?')) != '/':
    n = int(data)
    if n >= 2:
        limit = int(math.sqrt(n))
        for i in range(2,limit + 1):
            if n % i == 0:
                print(f"{n}は素数じゃないよ")
                break
        else:
            print(f"{n}は素数")
    else:
        print(f"{n}は2以上の整数を入力してね")

            