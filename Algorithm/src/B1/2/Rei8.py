rndnum = 13  # グローバル変数の定義

def irnd():
    global rndnum
    rndnum = (rndnum * 109 + 1021) % 32768
    return rndnum

result = ''
for i in range(1000):
    result += f"{irnd():6d}"  # 6桁でフォーマット
    if (i + 1) % 40 == 0:  # 10個ごとに改行
        print(result)
        result = ''  # バッファをリセット
