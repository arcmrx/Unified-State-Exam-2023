for x in '0123456789abcde':
    a = int(f'123{x}5', 15) + int(f'1{x}233', 15)
    if a % 14 == 0:
        print(a, a // 14)