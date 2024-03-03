from itertools import *

sp = list(set(product('0123456', repeat=5)))
k = 0
for i in sp:
    if i[0] != '0':
        if i.count('6') == 1:
            ch = 0
            nech = 0
            for j in i:
                if int(j) % 2 == 0:
                    ch += int(j)
                else:
                    nech += int(j)
            if ch < nech:
                k += 1
print(k)
