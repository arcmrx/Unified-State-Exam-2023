x = '1' * 33 + '2' * 33 + '3' * 64
while '11' in x or '22' in x or '33' in x or '23' in x:
    x = x.replace('11', '2', 1)
    x = x.replace('22', '1', 1)
    x = x.replace('13', '2', 1)
    x = x.replace('23', '1', 1)
print(x)