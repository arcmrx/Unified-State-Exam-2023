x = '7' * 104
while '33333'in x or '777' in x:
    if '33333' in x:
        x = x.replace('33333', '7', 1)
    else:
        x = x.replace('777', '3', 1)
print(x)