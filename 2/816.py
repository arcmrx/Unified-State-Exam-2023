print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = not (x == (y <= z))
            print(x, y, z, int(F))
