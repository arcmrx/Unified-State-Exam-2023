for x in '0123456789abcdefg':
    a = int(f'10{x}0', 17) + int(f'f0{x}ff', 17)
    if a % 13 == 0:
        print(a // 13)