for n in range(1, 100):
    r = bin(n)[2:]
    r = r[::-1]
    if int(r, 2) == 13:
        print(n)
