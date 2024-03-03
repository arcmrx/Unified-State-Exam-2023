x = '7' * 116

while '333' in x or '7777' in x:
    if '333' in x:
        x = x.replace('333', '77', 1)
    else:
        x = x.replace('7777', '3', 1)
print(x)
