def F(n):
    if n <= 3:
        return 3
    if n % 2 == 0 and n > 3:
        return F(n // 2) + 5
    if n % 2 != 0 and n > 3:
        return F(n - 1) - F(n - 2)


print(F(20))
