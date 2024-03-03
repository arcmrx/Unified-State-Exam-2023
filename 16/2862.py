from functools import lru_cache


@lru_cache(None)
def F(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return F(n - 1) + 1
    if n > 0 and n % 2 == 0:
        return F(n / 2)


k = 0
for n in range(0, 1000000000):
    if F(n) == 2:
        k += 1
print(k)
