from fnmatch import fnmatch

for x in range(199999999, 100000000, -1):
    if fnmatch(str(x), '1*1*1?') and x % 19 == 0 and x % 6 == 0 and x % 2023 == 0:
        print(x)