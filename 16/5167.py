from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 2 == 0:
        return f(n + 2) - 3
    if n < 10000 and n % 2 != 0:
        return f(n + 2) + 1


print()
