def f(a, x, y):
    return (x * y > a) and (x > y) and (x < 8)


for a in range(1, 1000):
    if all(f(a, x, y) == 0 for x in range(1, 100) for y in range(1, 100)):
        print(a)
