for n in range(1, 10000):
    s = '13' * n
    while '13' in s or '31' in s or '11' in s:
        if '13' in s:
            s = s.replace('13', '4', 1)
        if '31' in s:
            s = s.replace('31', '1', 1)
        if '13' in s:
            s = s.replace('11', '2', 1)
        if '13' in s:
            s = s.replace('44', '1', 1)
    if sum(map(int, s)) < 100:
        print(n)
