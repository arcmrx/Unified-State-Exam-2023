def f(a, x):
    return ((x % 6 == 0) <= (x % 10 != 0)) or (x + a > 121)


for a in range(1, 100):
    if all(f(a, x) == 1 for x in range(1, 1001)):
        print(a)
