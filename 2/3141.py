print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (x <= y) and (z or y or ((not (y)) <= x))
            if not F:
                print(x, y, z)
