from itertools import *

k = 0
for x in product('АЛПЦЯ', repeat=5):
    s = ''.join(x)
    k += 1
    if s.count('А') <= 1 and 'Л' not in s and s.count('Ц') == 2:
        print(k, s)
        break
