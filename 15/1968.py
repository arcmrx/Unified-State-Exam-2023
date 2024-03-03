def f(x, a1, a2):
    return (170 <= x <= 580) <= (((not 290 <= x <= 800) and (not a1 <= x <= a2)) <= (not 170 <= x <= 580))


m = 10 ** 8
for a1 in range(100, 900):
    for a2 in range(a1 + 10, 900):
        if all(f(x, a1, a2) == 1 for x in range(100, 900)):
            m = min(m, a2 - a1)
print(m / 10)
