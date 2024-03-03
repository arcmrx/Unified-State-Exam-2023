from itertools import *

k = 0
for x in product('АЕЛМНОРЬ', repeat=6):
    s = ''.join(x)
    k += 1
    if 'НОРМАА' in s or 'НЕНОРМ' in s:
        print(k, s)
