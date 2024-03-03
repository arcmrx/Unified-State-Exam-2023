from fnmatch import fnmatch

for x in range(13, 10 ** 9 + 1, 13):
    if fnmatch(str(x), '24*68335') or fnmatch(str(x), '24*68935'):
        print(x, x // 129)
