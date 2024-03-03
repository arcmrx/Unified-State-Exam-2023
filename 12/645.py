x = '1' * 46 + '2' * 31
while '1111' in x:
    x = x.replace('1111', '2', 1)
    x = x.replace('222', '1', 1)
print(x)