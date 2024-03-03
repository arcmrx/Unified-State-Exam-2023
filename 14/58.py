x = 64 ** 30 + 2 ** 300 - 4
s = ''
while x != 0:
    s += str(x % 8)
    x //= 8
s = s[::-1]
print(s.count('7'))