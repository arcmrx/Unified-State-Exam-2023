def f(a, x):
    return (160 <= x <= 180) <= ((x % 35 == 0) <= (x % a == 0))


for a in range(1, 1000):
    if all(f(a, x) == 1 for x in range(1, 10001)):
        print(a)
