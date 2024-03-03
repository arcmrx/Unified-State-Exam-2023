from itertools import product
k = 0
for x in product('ПИТОНЯГА', repeat=8):
    s = ''.join(x)
    if s[0] != 'И' and s[0] != 'О' and s[0] != 'Я' and s[0] != 'А':
        if 'ИИ' not in s and 'ИО' not in s and "ИЯ" not in s and "ИА" not in s and 'ОИ' not in s and "ОО" not in s and "ОЯ" not in s and "ОА" not in s and "ЯИ" not in s and "ЯО" not in s and "ЯЯ" not in s and "ЯА" not in s and "АИ" not in s and "АО" not in s and "АЯ" not in s and "АА" not in s:
            k += 1
            print(k, s)

