for n in range(1, 1000):
    s = bin(n)[2:]
    s = s + str(s.count('1') % 2)
    s = s + str(s.count('1') % 2)
    s = int(s, 2)
    if s > 80:
        print(s)
