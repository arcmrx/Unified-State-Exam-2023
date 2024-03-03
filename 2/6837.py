print('1 2 3 4 5 F')
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                for x5 in range(2):
                    F = (x1 or not x2 or not x3 or x4 or not x5) and (not x1 or not x2 or x3 or x4 or x5) and (
                                x1 or not x2 or not x3 or not x4 or x5)
                    print(x1, x2, x3, x4, x5, int(F))
#00101