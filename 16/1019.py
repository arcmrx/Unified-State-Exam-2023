def F(n):
    if n <= 10:
        return n * n + 11
    if n > 10:
        return F(n - 3) + n * n - 5


print(F(40))
