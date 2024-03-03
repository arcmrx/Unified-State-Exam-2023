for x in range(0, 10000):
    m = 4 ** 2015 + 2 ** x - 2 ** 2015 + 15
    s = ''
    while m != 0:
        s += str(m % 2)
        m //= 2
    s = s[::-1]
    if s.count('1') == 500:
        print(x)
        break
