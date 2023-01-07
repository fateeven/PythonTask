# Программа, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Пример :
# абвгдабвгд -> 2
# абв

# a = input('Ввведите текст: ')
# b = input('Введите искомый элемент: ')
# if len(a) > len(b):
#     print(f'В тексте: {a} -> Элемент: {b} -> Найден: {a.count(b)} раз')
# elif a == b:
#     print(f'В тексте: {a} -> Элемент: {b} -> Найден: 1 раз')
# else:
#     print(f'Ошибка ввода')


def count_str(text_str, element_str):
    """определяет количество вхождений одной строки в другой"""
    if len(text_str) > len(element_str):
        print(f'В тексте: {text_str} \nЭлемент: {element_str} '
                  f'-> Найден: {text_str.count(element_str)} раз')
    elif text_str == element_str:
        print(f'В тексте: {text_str} \nЭлемент: {element_str} '
              f'-> Найден: 1 раз')
    else:
        print(f'Ошибка ввода')

    return text_str.count(element_str)


text = input('Ввведите текст: ')
element = input('Введите искомый элемент: ')
count_str(text, element)
