for n in range(1, 10000):
    r = bin(n)[2:]
    r = str(r)
    if n % 3 == 0:
        r = r + '1'
        r = '10' + r[:2]
    else:
        r = bin(((n % 3) * 2))[2:] + r
    if int(r, 2) > 8000:
        print(int(r, 2))
        break
