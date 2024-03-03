a = [int(s) for s in open('17_8504.txt')]
mn5 = min(el for el in a if 100 <= el <= 999 and el % 10 == 5)
res = []
for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if (100 <= x <= 999) or (100 <= y <= 999):
        if (x + y) % mn5 == 0:
            res += [x + y]
print(len(res), max(res))
