a = []
for n in range(1, 100):
    s = bin(n)[2:]
    s = str(s)
    if s.count('1') % 2 == 0:
        s = s + '0'
        s = '1' + s[2:]
    else:
        s = s + '1'
        s = '11' + s[2:]
    r = int(s, 2)
    if r > 25:
        if len(a) == 0:
            a = [n, r]
        elif a[1] > r:
            a = [n, r]
print(a[0])

