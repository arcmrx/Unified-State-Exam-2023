x = '>' + '1' * 11 + '2' * 12 + '3' * 30
while '>1' in x or '>2' in x or '>3' in x:
    if '>1' in x:
        x = x.replace('>1', '22>', 1)
    if '>2' in x:
        x = x.replace('>2', '2>', 1)
    if '>3' in x:
        x = x.replace('>3', '1>', 1)
print(x.count('2') * 2 + x.count('1'))
