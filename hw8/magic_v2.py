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
# data_test = [
#      {'name': 'Anton', 'games': 0, 'record': 999, 'avg_attempts': 0},
#      {'name': 'Max', 'games': 10, 'record': 5, 'avg_attempts': 2}
 ]


def check_credential(name):
    with open(BASE_DIR / 'credential.json', 'r') as f:
        player_data = json.load(f)
        print(player_data)
        for i in player_data:
            if i.get('name') == name:
                return i
            else:
                data = write_credential(name)
                return data
        #         data = {'name': name, 'games': 0, 'record': 999, 'avg_attempts': 0}
        #         return data


def write_credential(name):
    with open(BASE_DIR / "credential.json", "a") as f:
        data = {'name': name, 'games': 0, 'record': 999, 'avg_attempts': 0}
        data_new = json.dumps(data, indent=4)
        print(data_new, type(data_new))
        f.write(data_new)
        return data_new


name = input('Insert your name: ')

player_data = check_credential(name)
record = 0
most_attemts = 0


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
    # if record > most_attemts:
    #     most_attemts = record
    # attempts = 0
    # most_attemts = 0

    # сверяем введенное пользователем число со случайным
    if number > random_number:
        print("No, the Magic number less than", number)
    elif number < random_number:
        print("No, the Magic number greater than", number)
    else:
        print("\nCongratulations! The Magic number is", number)
        print("Attempts:", counter)
        player_data['games'] += 1
        print(player_data)
        #player_data['avg_attempts'] 
        if counter < player_data['record']:
            print('test_record')
            player_data['record'] = counter
            print(player_data)

        if input("\nContinue? (y/n) ") != "y":
            #write_credential()
            print('test', player_data)
            print('Bye!')
            break

        # если пользователь решил продолжить играть -
        # генерируем новое число и сбрасываем счетчик попыток
        random_number = random.randint(1, 10)
        counter = 0

