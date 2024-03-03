print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not((w or not(y)) and x)) or y == z
                if F == False:
                    print(x, y, z, w)
