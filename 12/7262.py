x = 60 * '4' + 60 * '6' + 60 * '8'
while '46' in x or '84' in x or '86' in x:
    if '46' in x:
        x = x.replace('46', '64', 1)
    if '84' in x:
        x = x.replace('84', '48', 1)
    if '86' in x:
        x = x.replace('86', '68', 1)
print(x[25] + x[75] + x[150])
