for x in '0123456789abc':
    a = int(f'537{x}623', 13) - int(f'6{x}35{x}2', 13)
    if a % 3 == 0:
        print(x)