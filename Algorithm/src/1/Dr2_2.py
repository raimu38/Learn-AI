text = 'ALGORITHM'
ango = ''
for i in text:
    ango += chr(ord(i) ^ 0x07)
print(ango)

decode = ''
for i in ango:
    decode += chr(ord(i) ^ 0x07)
print(decode)

#chr: 対応する整数をユニコード文字に変換する
#ord(i) : 文字をユニコードポイントに変換する
#^ 