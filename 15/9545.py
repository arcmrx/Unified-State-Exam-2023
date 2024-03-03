def f(a, x):
    return ((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (a <= x)


for a in range(1, 10000):
    if all(f(a, x) == 1 for x in range(1, 100001)):
        print(a)
