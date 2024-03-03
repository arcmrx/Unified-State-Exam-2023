p = {1, 3, 5, 7, 9, 11}
q = {3, 6, 9, 12}
a = set()


def f(x):
    return ((x in p) <= (x not in q)) or (x in a)


for x in range(1, 1000):
    if f(x) == 0:
        a.add(x)
print(sum(a))
