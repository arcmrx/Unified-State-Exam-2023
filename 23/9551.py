def f(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 3, b) + f(a * 2, b)


print(f(3, 30) * f(30, 105))
