def F(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a - 2, b) + F(a // 2, b)


print(F(40, 10) * F(10, 2))
