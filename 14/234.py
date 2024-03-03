x = 2 * 27 ** 7 + 3 ** 10 - 9
s = ''
while x != 0:
    s += str(x % 3)
    x //= 3
s = s[::-1]
print(s.count('0'))