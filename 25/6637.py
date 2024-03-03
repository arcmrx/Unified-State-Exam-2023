from fnmatch import fnmatch

for x in range(3052, 10 ** 10 + 1, 3052):
    if fnmatch(str(x), '1?2139*4'):
        print(x, x // 3052)
