def F(n):
    if n <= 0:
        return n
    if 0 < n < 10000 and n % 2 == 0:
        return F(n // 2) + n * 5
    if 0 < n < 10000 and n % 2 != 0:
        return F(n - 4) - F(n - 6)


print(F(70) + F(56) - F(66) - F(44))
