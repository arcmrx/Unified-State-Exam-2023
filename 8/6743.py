from itertools import *

k = 0
for x in product('АЙКОС', repeat=5):
    s = ''.join(x)
    k += 1
    if s.count('О') <= 1 and 'СС' not in s:
        print(k, s)
