for n in range(1, 1000):
    s = bin(n)[2:]
    s = str(s)
    if n % 2 == 0:
        s = "1" + s + '00'
    else:
        s = s + bin(s.count('1'))[2:]
    r = int(s, 2)
    if r > 190:
        print(n)
        break
