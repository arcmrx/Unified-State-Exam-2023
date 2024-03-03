for n in range(1, 100):
    if int('10', 7) <= n < int('100', 7) and int('100', 6) <= n < int('1000', 6) and n % 13 == 3:
        print(n)
