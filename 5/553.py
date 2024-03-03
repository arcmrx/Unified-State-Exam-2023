m = 0
for n in range(1, 1000):
    r = bin(n)[2:]
    r = str(r)
    r = r + str(r.count('1') % 2)
    r = r + str(r.count('1') % 2)
    if int(r, 2) < 80:
        m += 1
print(m)
