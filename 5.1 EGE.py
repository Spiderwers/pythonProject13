for n in range(0, 256):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    if len(s) < 8:
        s = '0' * (8 - len(s)) + s
    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', '0')
    r = int(s, 2)  # перевод в десятичную систему
    if r - n == 111:
        print(n)


a = []
for x in range(10, 1001):
    i = int(bin(x)[3:], 2)
    if x - i not in a:
        a.append(x-i)
print(len(a))