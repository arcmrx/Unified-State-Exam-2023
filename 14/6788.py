for x in range(0, 68):
    a = 5 + x * 68 + 3 * 68 ** 2 + 2 * 68 ** 3 + 1 * 68 ** 4
    b = 3 + 3 * 68 + 2 * 68 ** 2 + x * 68 ** 3 + 1 * 68 ** 4
    if (a + b) % 12 == 0:
        print(x, (a + b) // 12)