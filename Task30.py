#  Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

# Вариант 1

spisok = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {spisok}")
new_spisok = []
[new_spisok.append(i) for i in spisok if i not in new_spisok]
print(f"Список из неповторяющихся элементов: {new_spisok}")

# Вариант 2

from random import randint as rnd

mass = [rnd(1, 10) for i in range(12)]
print(f'Исходный список: {mass}')
print(f'Cписок неповторяющихся элементов: {list(set(mass))} ')