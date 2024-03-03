from fnmatch import fnmatch

for x in range(500000, 10 ** 10):
    if fnmatch(str(x), '*1?3'):
        d = 0
        for i in range(2, int(x // 2) + 2):
            if x % i == 0:
                d += 1
        if d == 3:
            print(x, x // 2)
