# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Пример:
# 4, 5 -> 20
# 4,6 -> 12
x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and(greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
print(f'{x}, {y} -> {calculate_lcm(x, y)}')