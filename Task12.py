# Программа, которая принимает на вход число N и выдаёт последовательность из N членов.
# - Для N = 5: 1, -3, 9, -27, 81

# Первое решение
N = int(input('Введите число: '))
s = 0
while s < N:
    print(f'{(-3) ** s}', end=', ')
    s += 1

print()  # /------

# Второе решение
n = int(input('Введите число: '))
for i in range(n):
    print(f'{(-3) ** i}', end=', ')

print()  # /------

# Третье решение

def row_powers3():
    n = int(input('Введите число: '))
    a = []
    for i in range(n):
        a.append((-3) ** i)
    print(a)

row_powers3()