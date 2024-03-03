def F(n):
    if n <= 2:
        return n
    if n > 2:
        return G(n) + F(n - 2)


def G(n):
    if n <= 2:
        return n
    if n > 2:
        return F(n - 1) - G(n - 2)


print(G(15))
