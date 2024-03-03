from fnmatch import fnmatch

for x in range(2023, 10 ** 10, 2023):
    if fnmatch(str(x), '1?2139*4'):
        print(x, x / 2023)
