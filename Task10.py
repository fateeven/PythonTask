#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input('Введите номер плоскости: '))
if x == 1:
    print('x > 0 and y > 0 ')
elif x == 2:
    print('x < 0 and y > 0')
elif x == 3:
    print('x < 0 and y < 0')
elif x == 4:
    print('x > 0 and y < 0')
else:
    print('Ошибка ввода')

# Второе решение
def coordinate_range():
    a = input('Введите номер плоскости: ')
    d = {'1':'x > 0 and y > 0', '2': 'x < 0 and y > 0', '3': 'x < 0 and y < 0', '4': 'x > 0 and y < 0'}

    print(d[a])



coordinate_range()