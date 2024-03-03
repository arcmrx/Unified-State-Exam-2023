def f(n):
    if n < 10:
        return 0
    else:
        return f(n // 10) + (n // 10 % 10) - (n % 10)


k = 0
for x in range(100):
    # При 10^2 => 1 единица, значит 10^10 => 9 единиц
    k += f(x) == 9
print(k)
# Ответ: 111111111
