file = open('24_5810.txt')
a = file.readline()
file.close()

while 'XY' in a or 'YZ' in a:
    if 'XY' in a:
        a = a.replace('XY', 'M')
    if 'YZ' in a:
        a = a.replace('YZ', 'M')

count, countm = 0, 0
for x in a:
    if x == 'M':
        count += 1
        if count > countm:
            countm = count
    else:
        count = 0
print(countm * 2)
