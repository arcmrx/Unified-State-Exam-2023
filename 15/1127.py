def f(a, x):
    return (a % 7 == 0) and ((240 % x == 0) <= ((a % x != 0) <= (780 % x != 0)))


for a in range(1, 10000):
    if all(f(a, x) == 1 for x in range(1, 100001)):
        print(a)