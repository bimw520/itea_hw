"""
    Обновите форму регистрации из hw5/reg_form.py таким образом, чтобы:

    1. Все данные пользователей сохранялись в файл users.txt в любом формате.
    2. В файл errors.txt записывать все ошибочные либо не валидные вводы.
        (не валидный номер телефона, email и т.д.)
"""
import re

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ERROR_TXT = Path(__file__).resolve().parent / "files"


def main():
    user_list = []

    while True:
        phone = get_phone()
        email = get_email()
        password = get_password()

        user_list.append([phone, email, password])
        save_data(phone, email, password)

        print(
            f"\nПоздравляем с успешной регистрацией!"
            f"\nВаш номер телефона: +{phone}"
            f"\nВаш email: {email}"
            f'\nВаш пароль: {"*"*len(password)}'
        )

        if input("Continue? (Y/n)") == "n":
            break

    print(user_list)

    with open(BASE_DIR / "users.txt", "a") as f:
        for phone, email, password in user_list:
            print(f"{phone} {email} {password}", file=f)


def save_data(phone, email, password):
    with open(BASE_DIR / "users.txt", "a") as f:
        print(f"{phone} {email} {password}", file=f)


# def get_phone():
#     phone = input("Введите номер телефона: ")
#     phone = re.sub(r"\D", "", phone)
#     return "380" + phone[-9:] if len(phone) > 8 else get_phone()


# 2 вариант функции получения номера телефона
def get_phone():
    phone = input("Enter phone number:")
    a = "".join(s for s in phone if s.isdigit())
    phone = "38" + a[-10:]

    if len(phone) != 12:
        print("Wrong format. Try again.")
        error_check(phone)
        return get_phone()
    return phone


def get_email():
    email = input("Введите email: ")
    if len(email) < 6 or email.count("@") != 1 or email.startswith("@"):
        print("Неверный формат. Повторите ввод.")
        return get_email()
        error_check(email)
    return email


# 2 вариант функции получения email (с регулярными выражениями)
# def get_email(message="Введите email: "):
#     email = input(message)

#     if not re.search(r"^[\w]+[\w.-]*@[\w.-]+\.[a-zA-Z]{2,}$", email):
#         return get_email("Неверный формат email. Повторите ввод: ")
#     return email


def get_password():
    password = input("Введите пароль: ")
    if len(password) < 8 or re.findall(r"\s", password):
        print("Пароль слишком простой. Придумайте более надежный пароль.")
        error_check(password)
        return get_password()

    u_counter = l_counter = d_counter = s_counter = 0
    for i in password:
        if i.isupper():
            u_counter += 1
        elif i.islower():
            l_counter += 1
        elif i.isdigit():
            d_counter += 1
        else:
            s_counter += 1

    if min(u_counter, l_counter, d_counter, s_counter) == 0:
        print("Пароль слишком простой. Придумайте более надежный пароль.")
        error_check(password)
        return get_password()

    if input("Повторите пароль: ") != password:
        print("Пароли не совпадают.")
        return get_password()
    return password


def error_check(tmp):
    with open(ERROR_TXT / "error.txt", "a+") as f:
        print(f"{tmp}", file=f)


if __name__ == "__main__":
    main()
