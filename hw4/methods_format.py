"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.

    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)

    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))

    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "some string".
        Результат: "some edited string".
    (Использовать форматирование строк f либо метод format)
"""

# можно заменить данную строку на input()
# string = 'Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY.' # noqa: E501

string = input('Insert string : ')
litt = bigg = 0

for i in string:
    if i.islower():
        litt += 1
    elif i.isupper():
        bigg += 1

if litt > bigg:
    result = string.lower()
elif litt < bigg:
    result = string.upper()
else:
    result = string.swapcase()

print(f'1. Исходная строка: {string}')
print(f'Результат: {result}')

# 2.
if string.istitle():
    result_2 = 'done. ' + string
else:
    result_2 = string.replace(string[:5], 'draft: ')

print(f'1. Исходная строка: {string}')
print(f'Результат: {result_2}')

# 3.
if len(string) < 20:
    result_3 = string.ljust(20, '@')
else:
    result_3 = string[:20]

print(f'1. Исходная строка: {string}')
print(f'Результат: {result_3}')
