for p in range(10, 36):
    for x in range(1, p):
        for y in range(1, p):
            a = x * p ** 3 + x * p ** 2 + x * p + 8
            b = 4 * p ** 3 + 3 * p ** 2 + x * p + 9
            c = y * p ** 3 + y * p ** 2 + 0 * p + 4
            if a + b == c:
                print(y * p ** 2 + y * p + x)
