# программа, которая будет на вход принимать число N и выводить числа от -N до N включительно.
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

N = int(input('Введите число: '))
s = -N
while s <= N:
    print(s)
    s = s + 1

# Второе решение
L = int(input('Введите число: '))
for i in range(-L, L+1):
    print(i)

# Третье решение
n = int(input('Введите число: '))
a = []
for i in range(-n, n+1):
    a.append(i)
print(a)


def row_numbers():
    """Выводит числа от -N до N включительно."""
    number = int(input('Введите число: '))
    row =[]
    for number in range(-number, number+1):
        row.append(number)
    print(row)


row_numbers()
