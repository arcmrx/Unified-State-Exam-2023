print('X Y Z W F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x <= (not(y <= z))) or w
                if not F:
                    print(x, y, z, w, int(F))

