a = [int(x) for x in open('17_6024.txt')]
pairs = []
m = max(x for x in a if x % 100 == 12) ** 2
for x, y in zip(a, a[1:]):
    if (x + y) ** 2 < m and ((x % 100 == 12) + (y % 100 == 12)) == 1:
        pairs.append(x + y)
print(len(pairs), max(pairs))
