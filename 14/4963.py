for x in '0123456789abcde':
    for y in '0123456789abcdefg':
        if (int(f'123{x}5', 15) + int(f'67{y}9', 17)) % 131 == 0:
            print(x, y, (int(f'123{x}5', 15) + int(f'67{y}9', 17)) // 131)
