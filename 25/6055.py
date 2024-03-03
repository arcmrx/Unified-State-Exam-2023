from fnmatch import fnmatch

for x in range(159, 10 ** 7 + 1, 159):
    if fnmatch(str(x), '2?1*67'):
        print(x, x // 159)
