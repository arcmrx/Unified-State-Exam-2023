def divs(n):
    return sorted({i for d in range(1, int(n ** 0.5) + 1) if n % d == 0 for i in (d, (n // d))})


for i in range(10 ** 9, 10 ** 12):
    if str(i) == str(i)[::-1]:
        d = divs(i)
        if d[-2] % 7 == 0:
            print(i, d[-2])
