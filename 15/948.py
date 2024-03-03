def f(a, x):
    return ((x % 4 != 3) or (x % 6 != 1)) <= (x % 36 != a)


for a in range(1, 10000):
    if all(f(a, x) == 1 for x in range(1, 100001)):
        print(a)