x = '1' + '0' * 33
while '1' in x or '100' in x:
    if '100' in x:
        x = x.replace('100', '0001', 1)
    else:
        x = x.replace('1', '00', 1)
print(x.count('0'))