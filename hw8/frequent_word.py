"""
    Реализуйте функцию, которая принимает текст и возвращает слово, которое
    в этом тексте встречается чаще всего.

    Напишите несколько тестов для функции.

    # Если таких слов несколько - приоритет у первого, если расположить список
    # в алфавитном порядке.
    # Например:
    text = "hi world, hi python. i am very cool but i am still learning."
    # чаще всего встречаются "hi", "i" и "am", но по алфавиту "am" - раньше
    assert frequent_word(text) == "am"

"""
text = "hi world, hi python. i am very cool but i am still learning."


def frequent_word(text):
    data = []
    final = []
    data_dict = {}
    word = ''
    for char in text:
        if char.isalpha():
            word += char
        elif word:
            data.append(word)
            word = ''
    for _ in data:
        if _ not in data_dict:
            data_dict[_] = data.count(_)
    for key, value in data_dict.items():
        if value:
            final.append(key)
    final.sort()
    return final[0]


assert frequent_word(text) == "am"
