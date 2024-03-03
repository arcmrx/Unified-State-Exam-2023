file = open('24_6757.txt')
a = file.readline()
file.close()

a = a.replace('CFE', 'X')
a = a.replace('FCE', 'X')

count = 0
countm = 0
for x in a:
    if x == 'X':
        count += 1
        if count > countm:
            countm = count
    else:
        count = 0
print(countm)
