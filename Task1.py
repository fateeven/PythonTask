# Вывести квадрат числа

n = int(input('Введите число: '))
print(f'Квадрат числа: {n ** 2}')


# функция выводит квадрат введенного числа
def squared():
    """Выводит квадрат введенного числа"""
    number = int(input('Введите число: '))
    print(f'Квадрат числа {number} = {number ** 2}')


squared()