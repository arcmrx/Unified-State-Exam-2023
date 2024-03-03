def F(x, y):
    return (x + y <= 32) or (y <= x + 4) or (y >= a)


for a in range(1000):
    if all(F(x, y) == 1 for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
