p = {3, 6, 9, 12}
q = {1, 2, 3, 4, 5, 6}
a = set()


def f(x):
    return not ((not (x in a)) and (x in p)) or not (x in q)


for x in range(1, 1000):
    if f(x) == 0:
        a.add(x)
print(len(a))
