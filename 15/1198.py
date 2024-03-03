def f(a1, a2, x):
    return ((180 <= x <= 520) <= (a1 <= x <= a2)) and ((not 160 <= x <= 410) or (a1 <= x <= a2))


m = 10 ** 8
for a1 in range(150, 600):
    for a2 in range(150, 600):
        if all(f(a1, a2, x) == 1 for x in range(150, 600)):
            m = min(m, a2 - a1)
print(m / 10)
