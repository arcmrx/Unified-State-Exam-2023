def f(x, a):
    return ((not (x % 84 == 0)) or (not (x % 90 == 0))) <= (not (x % a == 0))


for a in range(1, 10000):
    if all(f(x, a) == 1 for x in range(1, 100001)):
        print(a)
