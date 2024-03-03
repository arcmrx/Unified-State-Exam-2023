k = 0
for n in range(1, 101):
    x = '1' + '0' * n
    while '01' in x or '1' in x:
        if '10' in x:
            x = x.replace('10', '0001', 1)
        else:
            if '1' in x:
                x = x.replace('1', '0', 1)
    if len(x) % 7 == 0:
        k += 1
print(k)
