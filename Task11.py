#Программа, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
x_a = int(input('Введите x точки А '))
y_a = int(input('Введите у точки А '))
x_b = int(input('Введите x точки B '))
y_b = int(input('Введите у точки B '))

print(((x_a - x_b)**2 + (y_a - y_b)**2)**0.5)