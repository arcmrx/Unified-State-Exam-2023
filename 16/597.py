def f(n):
    if n <= 10:
        return n
    if 10 < n <= 36:
        return n // 4 + f(n - 10)
    if n > 36:
        return 2 * f(n - 5)


print((f(100)))
