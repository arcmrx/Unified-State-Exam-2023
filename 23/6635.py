d = set()


def f(c, step):
    if step == 13:
        d.add(c)
    else:
        f(c - 3, step + 1)
        f(c * (-3), step + 1)


f(333, 0)
print(len([x for x in d if x < 0]))
