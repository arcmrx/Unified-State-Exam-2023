print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (w == y) or (((not x) <= z) and ((not z) <= y))
                if not F:
                    print(x, y, z, w, int(F))