for x in '0123456789ABCDE':
    if (int(f'98{x}79641', 22) + int(f'25{x}43', 22) + int(f'63{x}5', 22)) % 21 == 0:
        print((int(f'98{x}79641', 22) + int(f'25{x}43', 22) + int(f'63{x}5', 22)) // 21)
        break
