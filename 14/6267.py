mx = []
for x in '0123456789abcdefghiklmnopqrstuvwxyz':
    a = int(f'12{x}45', 36) + 1 * 12345 + int(x, 36)
    if a % 13 == 0:
        mx.append(a // 13)
print(max(mx))
