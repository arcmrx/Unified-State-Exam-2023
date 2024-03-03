from itertools import product

c = 0
for x in product('ПЯТНИЦА', repeat=5):
    x = ''.join(x)
    if x.count('Я') == 1 and x[0] != 'Н':
        c += 1
print(c)
