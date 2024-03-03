for n in range(1, 100):
    b = bin(2 * n)[2:]
    if bin(n).count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    if b.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    r = int(b, 2)
    if r > 249:
        print(n)
        break
