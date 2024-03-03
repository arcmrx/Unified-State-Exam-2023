from fnmatch import fnmatch

for x in range(27, 10 ** 8, 27):
    if fnmatch(str(x), '123*890'):
        print(x, x/27)
