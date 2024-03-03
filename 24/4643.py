file = open('24_4643.txt')
a = file.readline()
file.close()

a = a.replace('12B', 'X')
a = a.replace('21A', 'X')
a = a.replace('22A', 'X')
a = a.replace('22B', 'X')
a = a.replace('11A', 'X')
a = a.replace('11B', 'X')
a = a.replace('12A', 'X')
a = a.replace('21B', 'X')


count, countm = 0, 0
for x in a:
    if x == 'X':
        count += 1
        if count > countm:
            countm = count
    else:
        count = 0
print(countm)
