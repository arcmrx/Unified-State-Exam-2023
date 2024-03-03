for n in range(1, 16):
    r = bin(n)[2:]
    r = str(r)
    if r.count('1') % 2 == 0:
        r = r + '1'
        r = '10' + r[2:]
    else:
        r = r + '0'
        r = '11' + r[2:]
    print(int(r, 2))
