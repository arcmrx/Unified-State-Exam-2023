for a in range(-100, 100):
    for b in range(-100, 100):
        x = -5 + 4 * (5 + a) + 90
        y = 15 + 4 * (1 + b) + 4
        if x == 5 and y == 3:
            print(a, b)
