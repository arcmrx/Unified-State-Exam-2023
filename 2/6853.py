print('X Y Z W')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y) or (z <= w)) and not (x <= w)
                if F:
                    print(x, y, z, w)
