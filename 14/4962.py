for x in '0123456789a':
    if int(f'3364{x}', 11) + int(f'{x}7946', 12) == int(f'55{x}87', 14):
        print(int(f'55{x}87', 14))