from fnmatch import fnmatch

for x in range(1, 10 ** 7 + 1):
    if fnmatch(str(x), '12*348') and x % 12 == 0:
        d = 2
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                d += 2
        if d == 12:
            print(x, x // 2)
