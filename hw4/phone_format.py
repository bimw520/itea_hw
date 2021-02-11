"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 099 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в формате: 380501234567.

    Если цифр в номере недостаточно, чтобы описать номер в нужном формате -
        попросить пользователя повторить ввод.
"""
import re
tel = ''
while True:
    phone = input('Enter phone number: ')

    for i in phone:
        if i.isdigit():
            tel += i

    if a := re.search('[6,5,7,9]{1}[0,3,6,7]{1}[0-9]{7}', tel):
        print(f'380{a.group()}')
        break
    else:
        print('Please check the phone number and try again')
        continue
