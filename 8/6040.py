from itertools import *

k = 0
for x in product('0123456', repeat=6):
    s = ''.join(x)
    if s.count('6') == 1 :
        k += 1
print(k)
