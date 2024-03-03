for x in '0123456789abc':
    a = int(f'753{x}2', 13) + int(f'2{x}173', 13)
    if a % 12 == 0:
        print(x, a // 12)
