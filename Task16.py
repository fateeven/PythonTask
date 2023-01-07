# Задайте список из n чисел последовательности (1 + 1/n)**n,
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

num = int(input('Введите число: '))
result = [round((1 + 1 / i) ** i, 2) for i in range(1, num + 1)]
print(f'Список чисел: {result} ')
print(f'Сумма чисел в списке: {sum(result)} ')


def list_of_numbers(number):
    """Задает список из number чисел последовательности-(1 + 1/n)**n"""
    n = 1
    list = []
    while n < number + 1:
        result = (1 + 1 / n) ** n
        n += 1
        list.append(round(result, 2))

    print(f'Список чисел: {list} ')
    print(f'Сумма чисел в списке: {sum(list)} ')


nums = int(input(f'Введите число: '))
list_of_numbers(nums)
