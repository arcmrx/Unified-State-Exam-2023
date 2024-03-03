for n in range(1, 1000):
    a = []
    k = 0
    s = bin(n)[2:]
    s = str(s)
    if s.count('1') % 2 == 0:
        s = '10' + s
    else:
        s = '11' + s
    if s.count('1') % 2 != 0:
        s = s + '11'
    else:
        s = s + '00'
    r = int(s, 2)
    if r < 860:
        k += 1
    a.append(k)
    print(k)
