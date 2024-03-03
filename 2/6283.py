print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not (not (x <= (not (w))) and z)) and (not (w <= z)) and (x <= (not (z)))
                print(x, y, z, w, int(F))
