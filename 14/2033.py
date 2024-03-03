m = 6 * 144 ** 26 + 11 * 12 ** 75 - 48
s = ''
while m != 0:
    s += str(m % 12)
    m //= 12
s = s[::-1]
print(s.count('11'))
