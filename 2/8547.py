print('a b c t F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for t in range(2):
                F = ((not a) or (not b)) and (c <= (not a)) and ((t and (not a)) or (c and (not b)))
                if a != 1:
                    print(a, b, c, t, int(F))
