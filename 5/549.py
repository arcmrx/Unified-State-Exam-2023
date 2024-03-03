for n in range(1, 1000):
    r = bin(n)[2:]
    r = str(r)
    if int(r) % 2 == 0:
        r = r + '0'
    else:
        r = r + '1'
    if r.count('1') % 2 == 0:
        r = r + '0'
    else:
        r = r + '1'
    if r.count('1') % 2 == 0:
        r = r + '0'
    else:
        r = r + '1'
    if int(r, 2) > 130:
        print(n)
        break
