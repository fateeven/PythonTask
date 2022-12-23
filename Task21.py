# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5])

# Первое решение
spisok = list(map(int, input('Введите числа через пробел: ').split()))
print(f'Список: {spisok}')

long = 0
new_spisok = 0
if len(spisok) % 2 != 0:
    long = len(spisok) // 2 + 1
else:
    long = len(spisok) // 2

new_spisok = [spisok[i] * spisok[len(spisok) - i - 1] for i in range(long)]
print(f'Новый список: {new_spisok}')


# Второе решение, с помощью написанного метода и встроенных в него функций
def pair_multi(nums: list[int]) -> list:  # метод возвращает список произведений пар элементов
    pairs = []
    iterations = int(round((len(nums) + 1) / 2))
    for i in range(iterations):
        pairs.append(nums[i] * nums[len(nums) - 1 - i])
    return pairs


print(pair_multi(spisok))

# Третье решение
import random
from operator import length_hint
a= [random.randint(2, 9) for i in range(random.randint(1, 7))]
print(f'\nСписок = {a} => {[(a[i]*a[-i-1]) for i in range((len(a)+1)//2)]}')