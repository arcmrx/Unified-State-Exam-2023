from itertools import *

k = 0
for x in product('АРБУЗ', repeat=6):
    s = ''.join(x)
    if s.count('А') == 3 and 'ААА' not in s and 'АА' in s:
        print(s)
        k += 1
print(k)
