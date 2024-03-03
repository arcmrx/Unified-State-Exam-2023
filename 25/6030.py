from fnmatch import fnmatch

for x in range(129, 10 ** 8 + 1, 129):
    if fnmatch(str(x), '12?3*46'):
        print(x, x // 129)
