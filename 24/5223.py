s = open('24_5223.txt').readline()

while 'DD' in s:
    s = s.replace('DD', 'D D')
m = 0
for x in s.split():
    if 'FE' in x:
        m = max(m, len(x))
print(m)
