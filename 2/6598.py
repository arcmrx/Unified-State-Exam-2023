print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= w) and ((not y) <= z)) <= ((z == x) or (w and (not y)))
                if not F:
                    print(x, y, x, w, int(F))
