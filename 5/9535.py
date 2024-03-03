for n in range(1, 1000):
    r = bin(n)[2:]
    r = str(r)
    if n % 2 == 0:
        r = r + '0'
    else:
        r = r + '1'
    if r.count('1') != 0:
        r = r + '1'
    else:
        r = r + '0'
    if int(r, 2) > 2023:
        print(int(r, 2))
        break
