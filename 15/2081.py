from itertools import product

p = ['11' + ''.join(i) for i in list(product(['0', '1'], repeat=6))]
q = [''.join(i) + '0' for i in list(product(['0', '1'], repeat=7))]
ca = [''.join(i) for i in list(product(['0', '1'], repeat=8))]
cx = [''.join(i) for i in list(product(['0', '1'], repeat=8))]
for i in range(len(ca) - 1, -1, -1):
    y = ca[i]
    del ca[i]
    f = True
    for x in cx:
        c = (not (x in ca)) <= ((x in p) or (not (x in q)))
        if not c:
            f = False
            break
    if not f:
        ca.append(y)
print(len(ca))
