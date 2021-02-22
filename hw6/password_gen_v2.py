"""
    Обновите генератор паролей из hw5/password_gen.py таким образом, чтобы:

    1. Все сгенерированные пароли записывались в файл.
    2. После генерации пароля, сравнить его с содержимым файла.
        Если в файле уже записан такой пароль,
        то вывести сообщение с предупреждением "Insecure password".

    *3. Программа должна генерировать только уникальные пароли.
        Если в результате пункта 2 пароль уже содержится в файле, то генерируем
        его заново.

    * дополнительно стоит обрабатывать количество попыток генерации,
    так как после того, как будут сгенерированы все возможные комбинации,
    программа зациклится либо уйдет в бесконечную рекурсию и сломается

"""

from random import choice, randint
import string
from pathlib import Path


path = Path(__file__).resolve().parent


def main():
    stage_pass = input(
 "\tменю\n"
 "1. сгенерировать простой пароль\n"
 "2. сгенерировать средний пароль\n"
 "3. сгенерировать сложный пароль\n"
 "4. генерация своего пароля\n"
    )

    if stage_pass == '1':
        test = get_pass(string.ascii_lowercase)

    elif stage_pass == '2':
        test = get_pass(string.ascii_letters + string.digits)

    elif stage_pass == '3':
        test = get_hard_pass(string.digits + string.ascii_letters + string.punctuation)

    elif stage_pass == '4':
        self_pass = input('Введите свои символы для пароля: ')
        for i in self_pass:
            if i == ' ':
                i = i.string.replace(' ', '')
        test = get_pass(self_pass)

    print(test)


def len_pass():
    len_pas = input('Введите длинну пароля: ')
    len_pas = int(len_pas) if len_pas else 8
    print(len_pas)
    if len_pas < 8:
        print('len pass < 8 is not secure ')
        return len_pass()
    return len_pas


def get_pass(_):
    tmp = ''
    encrypt = _
    numb = len_pass()
    for i in range(numb):
        tmp += choice(encrypt)
    if save_to_file(tmp) is not True:
        return get_pass(encrypt)
    return tmp


def get_hard_pass(_):
    tmp = ''
    encrypt = _
    len_pass = randint(8, 16)
    u_counter = l_counter = d_counter = s_counter = 0
    for i in range(len_pass):
        tmp += choice(encrypt)
        for a in tmp:
            if a.isupper():
                u_counter += 1
            elif a.islower():
                l_counter += 1
            elif a.isdigit():
                d_counter += 1
            else:
                s_counter += 1

    if min(u_counter, l_counter, d_counter, s_counter) == 0:
        print('Insecure password')
        return get_hard_pass(encrypt)
    elif save_to_file(tmp) is not True:
        print('This password is in base, test')
        return get_hard_pass(encrypt)
    return tmp


def save_to_file(tmp):
    with open(path / "userpass.txt", "a+") as f:
        chek = f.readlines()
        for i in chek:
            if i.startswith(tmp):
                return False
        print(tmp, file=f)
    return True


if __name__ == '__main__':
    main()
