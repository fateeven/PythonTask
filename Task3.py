# Программа, которая на вход принимает 5 чисел
# и выдает максимальное из них

max_number = int(input('Введите число: '))
for i in range(4):
    number = int(input('Введите число: '))
    if number > max_number:
        max_number = number
print(f'Максимальное число: {max_number}')


# Второе решение

a = list(map(int, input('Введите 5 чисел через пробел: ').split())) # map - присваевает каждому числу тип int
print(f'Максимальное число: {max(a)}')                             # max - встроенная функция, показывает макс. элемент