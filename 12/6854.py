x = '7' * 256
k = 0
while '7777' in x or '1111' in x:
    if '7777' in x:
        x = x.replace('7777', '1', 1)
        k += 4
    if '1111' in x:
        x = x.replace('1111', '7', 1)
print(k)
