# for n in range(1, 101):
#     k = n
#     r = ''
#     l = ''
#     while n != 0:
#         r = str(n % 3) + r
#         n //= 3
#     r = r[::-1]
#     if k % 3 != 0:
#         m = ((k % 3) * 5)
#         while m != 0:
#             l = str(m % 3) + l
#             m //= 3
#         l = l[::-1]
#         r = r + l
#     if int(r, 3) > 146:
#         print(k)
def per(x):
    s = ''
    while x > 0:
        s = str(x % 3)
        x //= 3
    return s


for n in range(1, 1000):
    x = per(n)
    if n % 3 == 0:
        x += x[-2:]
    else:
        x += str(per(n % 3 * 5))
    r = int(x, 3)
    if r >= 146:
        print(n)
        break
