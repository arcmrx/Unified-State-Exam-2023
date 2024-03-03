from fnmatch import fnmatch

for x in range(23, 10 ** 8 + 1, 23):
    if fnmatch(str(x), '2*5443?1'):
        print(x, x // 23)
