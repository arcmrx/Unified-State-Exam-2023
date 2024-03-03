print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not y) and x and ((not z) or w)
                if F:
                    print(x, y, z, w, int(F))
