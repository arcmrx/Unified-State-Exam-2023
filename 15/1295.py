def f(a1, a2, x):
    return (170 <= x <= 540) <= (((370 <= x <= 830) and (not a1 <= x <= a2)) <= (not 170 <= x <= 540))


m = 10 ** 8
for a1 in range(150, 900):
    for a2 in range(150, 900):
        if all(f(a1, a2, x) == 1 for x in range(150, 900)):
            m = min(m, a2 - a1)
print(m/10)
