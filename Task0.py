# Программа, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# т.е. факториал N
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math

num = int(input("Введите число: "))
result = [math.factorial(i) for i in range(1, num + 1)]  # использую встроенную функцию math.factorial(i)
print(f'Произведений чисел равно: {result}')


# Второе решение, создам метод

#Метод вычисления факториала N
def mult(num: int) -> str:    # -> str, определяем какого типа будет return
    str_mult = '1'
    for i in range(2, num + 1):
        str_mult += f'*{i}'
    return str_mult

num = int(input("Введите число: "))
example = [mult(i) for i in range(1, num + 1)]
print(f'Пример вычесления: {example}')
