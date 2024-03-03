from itertools import *

k = 0
for x in product('01234567', repeat=5):
    s = ''.join(x)
    if s.count('6') == 1 and s[
        0] != '0' and '16' not in s and '61' not in s and '36' not in s and '63' not in s and '56' not in s and '65' not in s and '76' not in s and '67' not in s:
        k += 1
print(k)
