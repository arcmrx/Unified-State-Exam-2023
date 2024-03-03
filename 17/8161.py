a = [int(s) for s in open('17_8161.txt')]
ans = []
m3 = max(s for s in a if 100 <= s <= 999)
for x, y in zip(a, a[:1]):
    if ((100 <= abs(x) <= 999) != (100 <= abs(y) <= 999)) and (x + y <= m3):
        ans.append(x + y)
print(len(ans), max(ans))
