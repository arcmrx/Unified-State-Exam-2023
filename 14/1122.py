for x in range(1, 1000):
    m = 36 ** 17 - 6 ** x + 71
    s = 0
    while m != 0:
        s += m % 6
        m //= 6
    if s == 61:
        print(x)
