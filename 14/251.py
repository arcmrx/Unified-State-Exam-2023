for n in range(2, 20):
    if 68 % int('10', n) == 2 and int('1000', n) <= 68 <= int('10000', n):
        print(n)
