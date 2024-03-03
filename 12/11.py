x = '8' * 70
while '2222' in x or '8888' in x:
    if '2222' in x:
        x = x.replace('2222', '88', 1)
    else:
        x = x.replace('8888', '22', 1)
print(x)
