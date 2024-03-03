for n in range(1, 30):
    r = bin(n)[2:]
    r = str(r)
    if r.count('1') % 2 == 0:
        r = '10' + r
        r = r[:-2] + '00'
    else:
        r = '11' + r
        r = r[:-2] + '11'
    print(int(r, 2))
