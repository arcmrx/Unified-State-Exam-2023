from itertools import *

k = 0
for x in product('012345678', repeat=7):
    s = ''.join(x)
    if s.count('8') == 1 and s[0] not in '01357' and s[-1] not in '02468':
        k += 1
print(k)
