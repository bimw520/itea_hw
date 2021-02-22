"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""
from pathlib import Path


path = Path(__file__).resolve().parent
file_path = path / "files"

with open(file_path / "file_practice.txt", "w") as f:
    f.seek(0)
    f.write("Starting practice with files\n")
"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""
with open(file_path / "file_practice.txt", "r") as f:
    print(f.read(5).upper())
    f.seek(0)
    print(f.read())


"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""
with open(file_path / "text.txt", "a+") as f:
    f.seek(0)
    tmp = f.read()
    count_i = tmp.count('i')
    count_e = tmp.count('e')
    if count_i > count_e:
        word = tmp.replace('i', 'e')
    else:
        word = tmp.replace('e', 'i')
    f.write(word)
"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""
with open(file_path / "file_practice.txt", "a+") as f:
    f.seek(0)
    tmp = f.read()
    count = len(tmp)
    if count % 2:
        f.write('bye')
    else:
        f.write('the end')

"""
    5.
    В средину файла file_practice.txt вставить строку " *some inserted text* "
    (средина - имеется в виду средина текста)
"""
with open(file_path / "file_practice.txt", "r+") as f:
    f.seek(0)
    tmp = f.read()
    count = int(len(tmp) / 2)
    tmp = tmp[count:]
    f.seek(count)
    f.write(' *some inserted text* ' + tmp)
