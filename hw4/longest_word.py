"""
    Вводится строка.

    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

string = input('Введите строку: ')
kol_slov = 0
temp = _ = 0

for i in string:
    _ += len(i)
    if temp < _:
        temp = _
    if i == ',' or i == ' ':
        kol_slov += 1
        _ = 0

print('naibolshee slovo: ', temp)
print('slov v stroke: ', kol_slov)
