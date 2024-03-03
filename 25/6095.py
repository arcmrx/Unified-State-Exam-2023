from fnmatch import fnmatch

for x in range(1, 10 ** 8 + 1):
    if fnmatch(str(x), '*15*7424') and (x % 111 == 0 or x % 113 == 0 or x % 127 == 0):
        if x % 111 == 0:
            print(x, x // 111)
        elif x % 113 == 0:
            print(x, x // 113)
        elif x % 127 == 0:
            print(x, x // 127)
