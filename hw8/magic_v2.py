"""
    Реализуйте игру Magic (hw3/magic.py) с некоторыми дополнениями.

    1. При запуске, программа спрашивает имя игрока.

    2. В словаре player_data хранить данные игрока и актуализировать их после
    каждой сыгранной игры. Оперировать такими данными:
        name - имя игрока
        games - общее количество сыграных игр
        record - рекордное количество попыток (минимальное)
        avg_attempts - среднее количество попыток за игру

    3. При выходе из программы данные игрока записывать в файл (txt либо json).

    **4. При запуске программы, после ввода имени пользователем, читать файл,
    если данные об игроке есть в файле то загружать их в player_data.

"""
import random
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent / 'practice'


def check_credential(name):
    with open(BASE_DIR / 'credential.json', 'r') as f:
        player_data = json.load(f)
        print(player_data)
        for i in player_data:
            print(i)
            if i.get('name') == name:
                return i
        data = {'name': name, 'games': 0, 'record': 999, 'avg_attempts': 0}
        return data


def write_credential(name):
    with open(BASE_DIR / "credential.json") as f:
        data_new = json.load(f)
        for i in data_new:
            if i.get('name') == name.get('name'):
                i.update(name)
                break
            else:
                data_new.append(name)
        print('test_write: ', data_new)
    with open(BASE_DIR / "credential.json", 'w') as f:
        data = json.dumps(data_new, indent=4)
        f.write(data)


name = input('Insert your name: ')

player_data = check_credential(name)
print(player_data, type(player_data))
# record = 0
# most_attemts = 0


random_number = random.randint(1, 10)  # случайное число от 1 до 100
counter = 0  # счетчик попыток
print("Guess the Magic number!\n")

while True:

    try:
        number = int(input("The Magic number is "))  # записываем +1 попытку, если пользователь вводит число
        counter += 1
    except ValueError:
        print("You must enter a number.")
        continue

    # сверяем введенное пользователем число со случайным
    if number > random_number:
        print("No, the Magic number less than", number)
    elif number < random_number:
        print("No, the Magic number greater than", number)
    else:
        print("\nCongratulations! The Magic number is", number)
        print("Attempts:", counter)
        player_data['avg_attempts'] = (player_data['games'] \
        * player_data['avg_attempts'] + counter) \
        / (player_data['games'] + 1)
        player_data['games'] += 1
        if counter < player_data['record']:
            player_data['record'] = counter

        if input("\nContinue? (y/n) ") != "y":
            write_credential(player_data)
            print('Bye!')
            break

        # если пользователь решил продолжить играть -
        # генерируем новое число и сбрасываем счетчик попыток
        random_number = random.randint(1, 10)
        counter = 0

