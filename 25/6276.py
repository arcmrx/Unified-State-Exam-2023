from fnmatch import fnmatch

for x in range(2023, 10 ** 10 + 1, 2023):
    if fnmatch(str(x), '1?1?1?1*1') and sum(map(int, str(x))) == 22:
        print(x, x // 2023)
