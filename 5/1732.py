for n in range(1, 1000):
    r = bin(2*n)[2:]
    r = str(r)
    r = r + str((r.count('1')) % 2)
    r = r + str(r.count('1') % 2)
    if int(r, 2) > 1017:
        print(n)
        break