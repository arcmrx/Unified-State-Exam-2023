print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or not y) and not (y == z) and w
                if F == True:
                    print(x, y, z, w, F)
