def f(s, c, m):
    if s >= 351:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(s + 1, c + 1, m), f(s + 4, c + 1, m), f(s * 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


print('19', [s for s in range(1, 351) if f(s, 0, 2)])
print('20', [s for s in range(1, 351) if not f(s, 0, 1) and f(s, 0, 3)])
print('21', [s for s in range(1, 351) if not f(s, 0, 2) and f(s, 0, 4)])
