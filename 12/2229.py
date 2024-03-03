for x5 in range(1, 100):
    x = '5' * x5
    while '555' in x or '888' in x:
        x = x.replace('555', '8', 1)
        x = x.replace('888', '55', 1)
    print(x)
