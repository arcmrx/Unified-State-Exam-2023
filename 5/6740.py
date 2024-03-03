for n in range(100, 1, -1):
    s = bin(n)[2:]
    s = str(s)
    if n % 2 == 0:
        s = "10" + s
    else:
        s = "1" + s + '01'
    r = int(s, 2)
    if n < 8:
        print(r)
        break
