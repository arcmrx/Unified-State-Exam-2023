for x in range(10 ** 9, 10 ** 10):
    if str(x) == str(x)[::-1]:
        d = 0
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                d += 2
        if d % 7 == 0:
            print(x)
