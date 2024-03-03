x = '2' + '5' * 81
while '25' in x or '355' in x or '4555' in x:
    if '25' in x:
        x = x.replace('25', '4', 1)
    if '355' in x:
        x = x.replace('355', '2', 1)
    if '4555' in x:
        x = x.replace('4555', '3', 1)
print(x)