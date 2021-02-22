"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.

    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)

    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер

    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.

    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа

    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.

    Программа выводит сообщение:

    Поздравляем с успешной регистрацией!
    Ваш номер телефона: +380501234567
    Ваш email: example@mail.com
    Ваш пароль: ********** (кол-во  == кол-ву символов пароля)

"""
import string


def main():
    print(
        'Форма регистрации в базе!'
    )
    tel = reg_telefon()
    email = reg_email()
    passw = reg_pass()
    encrypt_pass = encrypt(passw)
    print(
        'Поздравляем с успешной регистрацией!\n'
        f'Ваш номер телефона: {tel}\n'
        f'Ваш email: {email}\n'
        f'Ваш пароль: {encrypt_pass}\n'
    )


def reg_telefon():
    tel = ''
    phone = input('Enter phone number: ')
    for i in phone:
        if i.isdigit():
            tel += i
    if len(tel) >= 9:
        phone = '380' + phone[-9:]
        return phone
    else:
        print('Wrong format.')
        return reg_telefon()


def reg_email():
    email = input('Введите email: ')
    if len(email) < 6:
        print('Имейл меньше 6-ти символов')
        return reg_email()
    elif email.count('@') != 1:
        print('проверьте правильность символа @')
        return reg_email()
    else:
        return email


def reg_pass():
    tmp = ''
    space = litt = big = digit = punct = 0
    passw = input('Введите пароль: ')
    #passw_repeat = 
    for i in passw:
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

    if litt and big and digit and punct and len(passw) > 7:
        return passw
    else:
        print('Пароль должен иметь цифру, большую букву,'
        'маленькую и знак пунктуации')
        space = litt = big = digit = 0
        return reg_pass()


def encrypt(passw):
    tmp = ''
    _ = len(passw)
    while _ > 0:
        tmp += '*'
        _ -= 1
    return tmp


if __name__ == '__main__':
    main()
