table = 'QWERTYUIOPASDFGHJKLZXCVBNM?'
ango = 'KSOIDHEPZ'
result = ''

for ai in ango:
    if 'A' <= ai and ai <= 'Z':
        index = ord(ai) - ord('A')
    else:
        index = 26
    result += table[index]

print(result)

