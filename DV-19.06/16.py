from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n - 2 + f(n - 1)


for i in range(1, 2025):
    f(i)
print(f(2023) - f(2021))
