from fnmatch import fnmatch

for x in range(28, 10 ** 9 + 1, 28):
    if fnmatch(str(x), '6323*353?'):
        print(x, x // 28)
