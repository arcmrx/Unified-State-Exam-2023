for n in range(1, 1000):
    r = ''
    s = []
    while n != 0:
        r += str(n % 3)
        n //= 3
        r = r[::-1]
    r = r + str(int(r) % 3)
    if int(r, 3) > 99:
        print(int(r, 3))
