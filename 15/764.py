def f(x, a):
    return ((x % 15 == 0) and (x % 21 != 0)) <= ((x % a != 0) or (x % 15 != 0))


for a in range(1, 10000):
    if all(f(x, a) == 1 for x in range(1, 100001)):
        print(a)
