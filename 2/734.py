print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = ((not x) and y and z) or ((not x) and (not z))
            if F:
                print(x, y, z, int(F))
