x = 2197 ** 50 - 169 ** 35 - 26
s = 0
while x != 0:
    if x % 13 == 12:
        s += 1
    x //= 13
print(s)