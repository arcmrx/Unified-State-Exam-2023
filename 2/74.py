print('a b c F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            F = (a and not c) or (not b and not c)
            print(a, b, c, int(F))
