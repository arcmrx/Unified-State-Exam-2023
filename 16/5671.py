from functools import lru_cache


@lru_cache(None)
def F(n):
    if n <= 10:
        return n
    if n >= 10000:
        return 1
    if n % 2 == 0:
        return n % 10 + F(n + 2)
    else:
        return F(n - 2) - (n - 1) % 10


for i in range(1, 10001, 2):
    F(i)
for i in range(10000, -1, -2):
    F(i)
print(F(4500) + F(5515))
