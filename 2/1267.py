print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((w <= y) or (not (y <= z))) and (not x) and (not (x == z))
                if F:
                    print(x, y, z, w, int(F))
