from fnmatch import fnmatch

for x in range(124579, 10 ** 8, 100):
    if fnmatch(str(x), '124*5*79') and x % sum(int(d) for d in str(x) if d in '13579') == 0:
        print(x, sum(map(int, (str(x)))))
