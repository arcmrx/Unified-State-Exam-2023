def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a < b:
        return f(a + 3, b) + f(a * 2, b)


print(f(3, 27) * f(27, 63))
