for n in range(1, 100):
    b = bin(n)[2:]
    b = str(b)
    if b.count('1') % 2 == 0:
        b = b + '0'
        b = '10' + b[2:]
    else:
        b = b + '1'
        b = '11' + b[2:]
    r = int(b, 2)
    if r > 40:
        print(n)
        break
