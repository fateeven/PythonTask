# программа, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

d = int(input('Введите число недели: '))

if d >= 6 and d <= 7:
    print('Выходной день')
elif d >= 1 and d <= 5:
    print('Будний день')
else:
    print('Ошибка ввода')
