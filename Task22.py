# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Первое решение
spisok = list(map(float, input("Введите числа через пробел: ").split()))

new_spisok = [round(i % 1, 2) for i in spisok if i % 1 != 0]
print(f'Новый список: {new_spisok}')
print(f'Разница: ', max(new_spisok) - min(new_spisok))


# Второе решение с помощью 2 методов
def separate_fraction(num: float) -> float:  # метод отделяет дробную часть от целой
    list_num = str(num).split('.')
    return float('0.' + list_num[1])


def max_vs_min_fraction(num_list: list[float]) -> float:  # возвращает разницу между max и min дробными значениями
    new_list = [separate_fraction(i) for i in num_list if int(i) != float(i)]
    print(f'Новый список: {new_list}')
    return max(new_list) - min(new_list)


print(f'Разница: ', max_vs_min_fraction(spisok))
