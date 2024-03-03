from itertools import *

k = 0
for x in product('012345678', repeat=5):
    s = ''.join(x)
    if s.count('3') == 1 and s[0] != '0' and s[0] != '1' and s[0] != '3' and s[0] != '5' and s[0] != '7' and s[4] != '1' and s[
        4] != '8':
        k += 1
print(k)
