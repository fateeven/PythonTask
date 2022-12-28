# polinom_functions for Task32 and Task33

import sympy
from random import randint as rnd


def create_polinom(k: int, simple: bool = True) -> str:
    '''' Метод генерирует полином со случайными коэффициентами степени "к"
    simple = False вернет полином без сокращения нулевых коэффициентов'''
    polinom = ''
    for i in range(k, -1, -1):
        polinom += f'{rnd(0, 2)}*x**{i}+'
        if i == 0:
            polinom += f'{rnd(0, 100)}*x**{i}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)


def create_pol_file(polinom: str, filename: str = 'new'):
    """ Записывает полином в файл, дополнительно можно указать имя файла"""
    with open(f'{filename}.txt', 'w') as f:
        f.write(polinom)
