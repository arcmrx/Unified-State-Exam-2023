file = open('24_9552.txt')
a = file.readline()
file.close()

a = a.replace('CSGO', 'X')
a = a.replace('PC', 'Y')

count = 0
countm = 0
for x in a:
    if x == 'X' or x == 'Y':
        if x == 'X':
            count += 4
            if count > countm:
                countm = count
        if x == 'Y':
            count += 2
            if count > countm:
                countm = count
    else:
        count = 0
print(countm)
