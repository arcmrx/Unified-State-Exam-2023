import math

p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
r = {12, 24, 36, 48, 60}
a = set()


def f(x):
    return (x not in a) <= (((x in p) and (x in q)) <= (x in r))


for x in range(1, 1000):
    if f(x) == 0:
        a.add(x)
print(math.prod(a))
