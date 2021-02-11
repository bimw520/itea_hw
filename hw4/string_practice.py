string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'

string = string.replace(',', '')
print(string)


# 2. Найти индекс самой последней буквы 's' в строке.
#    Результат: 53

print(string.rfind('s'))

# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6

print(string.lower().count('i'))

# 4. Найти и вывести срез строки.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)

a = len('simply dummy text')
b = string.find('simply dummy text')

print(string[b:b+a])  # Сильно не смійтесь, не зовсім зрозумів цього завдання

# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'

len_str = int(len(string) / 2)
print(string[:len_str] * 3 + string[len_str:])
