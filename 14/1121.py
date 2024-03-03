for x in range(0, 10000):
    m = 4 ** 1014 - 2 ** x + 12
    s = ''
    while m != 0:
        s += str(m % 2)
        m //= 2
    s = s[::-1]
    if s.count('0') == 2000:
        print(x)
        break
