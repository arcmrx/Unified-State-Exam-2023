from fnmatch import fnmatch

for x in range(53, 10 ** 7 + 1, 53):
    if fnmatch(str(x), '*2?2*') and str(x) == str(x)[::-1]:
        d = 1
        for i in range(2, int(x / 2) + 1):
            if x % i == 0:
                d += 1
                if d > 30:
                    print(x, x // 53)
                    break
