print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x == (not z)) <= ((x or w) == y)
                if not F:
                    print(x, y, z, w, int(F))
