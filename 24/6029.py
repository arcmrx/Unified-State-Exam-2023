a = open('24_6029.txt').readline()

a = a.replace('EF', 'X')
a = a.replace('FE', 'X')

count, countm = 0, 0
for x in a:
    if x == 'X':
        count += 1
        if count > countm:
            countm = count
    else:
        count = 0
print(countm * 2 + 1)



