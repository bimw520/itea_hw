"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(ticket_num):
    b = []
    ticket_num = [str(ticket_num)]
    for i in ticket_num:
        numb = int(len(i) / 2)
        for a in i:
            b.append(int(a))
    left = sum(b[0:numb])
    right = sum(b[numb:])
    if left == right:
        return True
    return False


assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True

print("All tests passed successfully!")
