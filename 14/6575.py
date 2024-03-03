s = 766 ** 66 + 15 ** 13 - 22
c = 0
while s > 0:
    if s % 13 == 12:
        c += 1
    s //= 13
print(c)
