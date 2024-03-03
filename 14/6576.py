s = 283 ** 382 + 9 ** 15 + 2 ** 3
b = 0
c = 0
while s > 0:
    if s % 14 == 11:
        b += 1
    if s % 14 == 12:
        c += 1
    s //= 14
print(abs(b - c))
