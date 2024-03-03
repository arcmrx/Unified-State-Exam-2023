x = 5 * 343 ** 8 + 4 * 49 ** 12 + 7 ** 14 - 98
s = ''
while x != 0:
    s += str(x % 7)
    x //= 7
s = s[::-1]
print('0', s.count('0'))
print('1', s.count('1'))
print('2', s.count('2'))
print('3', s.count('3'))
print('4', s.count('4'))
print('5', s.count('5'))
print('6', s.count('6'))