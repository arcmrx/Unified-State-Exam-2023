for x in '0123456789abcdefg':
    a = int(f'9759{x}', 17) + int(f'3{x}108', 17)
    if a % 11 == 0:
        print(a // 11)
