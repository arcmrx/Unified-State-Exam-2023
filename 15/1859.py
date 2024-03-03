def f(a, x, y):
    return (2 * x + y != 70) or (x < y) or (a < x)


for a in range(1, 1000):
    if all(f(a, x, y) == 1 for x in range(0, 100) for y in range(0, 100)):
        print(a)
