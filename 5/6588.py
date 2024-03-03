for n in range(1, 100):
    s = bin(n)[2:]
    s = str(s)
    s = s.replace('1', 'm')
    s = s.replace('0', '1')
    s = s.replace('m', '0')
    s = '1' + s
    if sum(map(int, s)) % 2 != 0:
        s = s + '1'
    else:
        s = s + '0'
    r = int(s, 2)
    if r > 180:
        print(n)
        break