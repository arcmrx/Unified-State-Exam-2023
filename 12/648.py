for m in range(1, 51):
    x = '6' * m
    while '66' in x:
        x = x.replace('66', '1', 1)
        x = x.replace('11', '2', 1)
        x = x.replace('22', '6', 1)
    if x == '21':
        print(m)
