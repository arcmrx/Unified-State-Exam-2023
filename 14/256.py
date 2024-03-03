for n in range(1, 100):
    if int('10', 6) <= n < int('100', 6) and int('100', 5) <= n < int('1000', 5) and n % 11 == 1:
        print(n)
