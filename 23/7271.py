def F(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a - 1, b) + F(a // 2, b)


print(F(30, 9) * F(9, 1))
