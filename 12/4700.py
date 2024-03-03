for m in range(0, 10):
    x = '>' + 39 * '0' + m * '1' + 39 * '2'
    while '>1' in x or '>2' in x or '>0' in x:
        if '>1' in x:
            x = x.replace('>1', '22>', 1)
        if '>2' in x:
            x = x.replace('>2', '2>', 1)
        if '>0' in x:
            x = x.replace('>0', '1>', 1)
    x = x[:-1]
    n = int(x)

    sum = 0

    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10

    a = sum
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        print(x, sum, m)
        break
