# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для получения случайного int

from random import randint  # добавляем библиотеку
import numpy as np


def new_list():
    """Создает список путем ручного ввода"""
    n_list = list(map(int, input('Введите числа через пробел: ').split()))
    print(f'Список: {n_list}')
    return n_list


def new_ramdom_list():
    """
    Создает создает отсартированный по возрастанию
    рандомный список из 10 чисел, значением от 1 до 100
    """
    r_list = sorted(np.random.randint(1, 100, 10))
    print(r_list)
    return r_list


def mix_list(mix):
    """Перемешивает входящий список и выводит его"""
    for i in range(len(mix) - 1):
        n = randint(0, len(mix) - 1)
        mix[i], mix[n] = mix[n], mix[i]

    print(f'Перемешанный список: {mix}')


mix_list(new_list())
mix_list(new_ramdom_list())
