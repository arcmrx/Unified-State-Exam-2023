a = [int(x) for x in open('17_6752.txt')]
k = len([x for x in a if x % 3 == 0])
ans = []
for i in range(len(a) - 1):
    if (a[i] < 0 or a[i + 1] < 0) and a[i] + a[i + 1] < k:
        ans.append(a[i] + a[i + 1])
print(len(ans), max(ans))
