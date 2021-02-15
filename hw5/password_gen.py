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
# import re


def main():
    stage_pass = int(input(
        "\tМЕНЮ\n"
    "1. Сгенерировать простой пароль\n"
    "2. Сгенерировать средний пароль\n"
    "3. Сгенерировать сложный пароль\n"
    "4. Генерация своего пароля\n"
    ))
    if stage_pass == 1:
        len_pass = randint(8, 16)
        pass_bad = 0
        # probleme with code
        while pass_bad == 0:
            test = genpasss(len_pass, stage_pass)
            for i in test:
                if i == i.isupper or i.islower or i.isdigit:
                    pass_bad = 1
            else:
                pass_bad == 0
                test = genpasss(len_pass, stage_pass)
    elif stage_pass == 4:
        self_pass = input('Введите свои символы для пароля: ')
        len_pass = int(input('Введите длинну пароля: '))

        for i in self_pass:
            if i == ' ':
                i = i.string.replace(' ', '')
        print(self_pass)
        print(len_pass)

        test = selfpass(len_pass, self_pass)
        print(test)

    else:
        len_pass = int(input('Введите длинну пароля: '))
        if len_pass <= 8:
            print('len pass < 8 is not secure ')
        test = genpasss(len_pass, stage_pass)
    print(test)
    

def selfpass(len_pass, self_pass):
    tmp = ''
    while len_pass > 0:
        tmp += choice(self_pass)
        len_pass -= 1
    return tmp


def genpasss(len_pass, stage_pass):
    tmp = ''
    while len_pass > 0:
        tmp += choice(lmh_pass(stage_pass))
        len_pass -= 1
    return tmp


def lmh_pass(stage_pass):
    if stage_pass == 1:
        _ = string.ascii_lowercase
    elif stage_pass == 2:
        _ = string.ascii_letters + string.digits
    elif stage_pass == 3:
        _ = string.digits + string.punctuation # + string.ascii_letters
    return _


if __name__ == '__main__':
    main()
