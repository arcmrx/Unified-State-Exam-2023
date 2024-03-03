s = 673 ** 7 + 67 ** 6 + 3 ** 3
k = 0
c = 0
while s > 0:
    if s % 12 == 10:
        k += 10
    if s % 12 == 8:
        c += 8
    s //= 12
print(k - c)
