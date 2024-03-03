def F(a, b):
    if a > b or a == 9 or b == 9:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a * 2, b)


print(F(2, 12) * F(12, 42))
