from fnmatch import fnmatch

for x in range(1, 10 ** 7):
    if fnmatch(str(x), '3*52?'):
        d = 2
        for i in range(2, int(x / 2) + 1):
            if x % i == 0:
                d += 1
        if d % 2 != 0:
            k = 2
            while k * k <= x:
                if x % k == 0:
                    print(x, x // k)
                    break
                k += 1
            else:
                print("Число-то простое...")
