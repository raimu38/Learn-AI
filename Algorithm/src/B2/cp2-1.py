print("2-1")
a = [10, -5, 0, 29, 6, 2, 77, 8]


for n in a:
    if n % 2 == 0:
        print(f"{n} は偶数です")
    else:
        print(f"{n} は奇数です")

print("2-2")

def expn(a, n):
    if a < 0:
        raise ValueError("aは負の値にできません")  # エラーメッセージを追加
    elif a == 0:
        return 1 if n == 0 else 0  # 0^0 = 1, 0^n = 0 (n > 0)
    else:
        if n == 0:
            return 1
        else:
            return a * expn(a, n - 1)

n = 10
try:
    exp3 = expn(3, n)
    exp2 = expn(2, n)
    result = exp3 - exp2
    print(result)
except ValueError as e:
    print(f"エラー: {e}")

