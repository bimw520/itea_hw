"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) данные владельцев,
    чьи имена начинаются на букву "m" либо заканчиваются на "а"
    (регистр не имеет значения).

    В файл записывать данные в таком формате:
    1. +380501234561 - Имя
    2. +380501234562 - Имя
    3. +380501234563 - Имя
    4. +380501234564 - Имя
"""


# def main():
#     pass


# if __name__ == "__main__":
#     main()

from pathlib import Path
path = Path(__file__).resolve().parent

with open(path / "userpass.txt", "r") as f:
    tmp = 'P0lkil012@'
    chek = f.readlines()
    
    for i in chek:
        print(i)
        if i.startswith(tmp):
            print('ALARM!!!')
            break