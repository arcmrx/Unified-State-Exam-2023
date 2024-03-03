x = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
s = ''
while x != 0:
    s += str(x % 6)
    x //= 6
s = s[::-1]
print(s.count('5') - s.count('0'))
