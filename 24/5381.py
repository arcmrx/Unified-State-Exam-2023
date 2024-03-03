from itertools import *

file = open('24_5381.txt')
a = file.readline()
file.close()
for x in product('ABCDEFU', repeat=3):
    s = ''.join(x)
    if (s[0] == 'B' or s[0] == 'C' or s[0] == 'D' or s[0] == 'F') and (s[1] == 'A' or s[1] == 'E' or s[1] == 'U') and (
            s[2] == 'B' or s[2] == 'C' or s[2] == 'D' or s[2] == 'F') and s in a:
        a = a.replace(s, 'XXX')

count, countm = 0, 0
for x in a:
    if x == 'X':
        count += 3
        if count > countm:
            countm = count
    else:
        count = 0
print(countm * 2)
