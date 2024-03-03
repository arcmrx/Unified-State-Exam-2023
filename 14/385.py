k = 0
for x in range(1, 700):
    if 16 <= x < 625 and x % 16 == 12:
        k = k + 1
print(k)
