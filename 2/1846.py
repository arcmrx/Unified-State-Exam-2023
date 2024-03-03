print('a b c d F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                F = ((not a) and (not b)) or (b == c) or d
                if not F:
                    print(a, b, c, d, int(F))
