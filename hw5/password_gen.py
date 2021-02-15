"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)

    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)


    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""  # noqa: E501
from random import choice, randint
import string


def main():
    stage_pass = input(
"\tМЕНЮ\n"
"1. Сгенерировать простой пароль\n"
"2. Сгенерировать средний пароль\n"
"3. Сгенерировать сложный пароль\n"
"4. Генерация своего пароля\n"
    )

    if stage_pass == '1':
        _ = string.ascii_lowercase
        len_pass = input('Введите длинну пароля: ')
        len_pass = int(len_pass) if len_pass else 8
        if len_pass <= 8:
            print('len pass < 8 is not secure ')
        test = genpasss(len_pass, _)

    elif stage_pass == '2':
        _ = string.ascii_letters + string.digits
        len_pass = input('Введите длинну пароля: ')
        len_pass = int(len_pass) if len_pass else 8
        if len_pass <= 8:
            print('len pass < 8 is not secure ')
        test = genpasss(len_pass, _)

    elif stage_pass == '3':
        tmp = ''
        space = litt = big = digit = punct = 0
        _ = string.digits + string.ascii_letters + string.punctuation
        len_pass = randint(8, 16)
        while True:
            test = genpasss(len_pass, _)
            for i in test:
                tmp += i
                if tmp.isspace():
                    space += 1
                elif i.islower():
                    litt += 1
                elif i.isupper():
                    big += 1
                elif i.isdigit():
                    digit += 1
                elif i in string.punctuation:
                    punct += 1
            if litt and big and digit and punct:
                break

    elif stage_pass == '4':
        self_pass = input('Введите свои символы для пароля: ')
        len_pass = int(input('Введите длинну пароля: '))

        for i in self_pass:
            if i == ' ':
                i = i.string.replace(' ', '')
        test = genpasss(len_pass, self_pass)

    print(test)


def genpasss(len_pass, _):
    tmp = ''
    while len_pass > 0:
        tmp += choice(_)
        len_pass -= 1
    return tmp


if __name__ == '__main__':
    main()
