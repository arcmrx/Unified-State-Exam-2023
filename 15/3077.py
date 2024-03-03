from functools import lru_cache


@lru_cache(None)
def F(x, y):
    return (680 * y + 256 * x < a) or (5 * x + 3 * y > 11111)


for a in range(2459234, 10 ** 7):
    if all(F(x, y) == 1 for x in range(1, 10 ** 5) for y in range(1, 10 ** 5)):
        print(a)
        break
