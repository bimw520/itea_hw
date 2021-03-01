"""
    1. Нарисовать границу из * в списке.

    [in]    ['python',
             'django']

    [out]   ['********',
             '*python*',
             '*django*',
             '********']

    [in]    ['abc',
             'def']

    [out]   ['*****',
             '*abc*',
             '*def*',
             '*****']

    Покрыть несколькими тестами.
"""


def draw_border(input_list: list) -> list:
    b = []
    for i in input_list:
        tmp = "*"*(len(i) + 2)
        b.append('*' + i + '*')
    b.insert(0, tmp)
    b.append(tmp)
    for i in b:
        print(i)


test = ['django', 'python']
draw_border(test)
