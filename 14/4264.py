x = 9 ** 11 * 3 ** 20 - 3 ** 9 - 27
s = ''
while x != 0:
    s += str(x % 3)
    x //= 3
s = s[::-1]
print(s.count('2'))
