for x in range(0, 1000):
    m = 125 ** 200 - 5 ** x + 74
    s = ''
    while m != 0:
        s += str(m % 5)
        m //= 5
    s = s[::-1]
    if s.count('4') == 100:
        print(x)
        break