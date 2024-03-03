def f(a, x, y):
    return (y + 3 * x > a) or (x < 20) or (y < 50)


for a in range(1000):
    if all(f(a, x, y) == 1 for x in range(100) for y in range(100)):
        print(a)
