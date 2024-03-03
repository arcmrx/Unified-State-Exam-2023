for a in range(-100, 100):
    for b in range(-100, 100):
        for c in range(-100, 100):
            x = 4 + 4 * (2 + a)
            y = 8 + 4 * (-4 + b)
            z = 10 + 4 * (-5 + c) + 2
            if x == 24 and y == 16 and z == 12:
                print(a, b, c)

