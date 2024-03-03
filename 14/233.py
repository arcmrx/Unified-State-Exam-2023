x = 3 * 16 ** 8 - 4 ** 5 + 3
s = ''
while x != 0:
    s += str(x % 4)
    x //= 4
s = s[::-1]
print(s.count('3'))