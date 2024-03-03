for n in range(1, 100):
    r = bin(n)[2:]
    r = str(r)
    if n % 2 == 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    if int(r, 2) > 52:
        print(int(r, 2))
