# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Вариант 1

num = int(input('Введите число: '))
dvoichnoe = ''

while num > 0:
    dvoichnoe = str(num % 2) + dvoichnoe
    num = num // 2
print(f'Двоичное число: {dvoichnoe} ')

# Вариант 2

num = int(input('Введите число: '))
print(bin(num)[2::])


# Вариант 3

def ordinary_bin(n: int) -> str:
    return bin(n)[2::]


print(ordinary_bin(45))
