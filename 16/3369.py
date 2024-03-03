from functools import lru_cache


@lru_cache(None)
def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return G(n) + F(n - 1)
    if n > 2 and n % 2 != 0:
        return F(n - 2) - 2 * G(n + 1)


def G(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return F(n - 3) + F(n - 2)
    if n > 2 and n % 2 != 0:
        return F(n + 1) - G(n - 1)


print(G(120))
