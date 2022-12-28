# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 6 -> [2,3]
# 144 -> [2,3]

# 1 вариант
num = int(input("Введите число: "))
i = 2  # первое простое число
spisok = []

while i <= num:
    if num % i == 0:
        spisok.append(i)
        num //= i  # Деление с остатком и присваивание (//=)
    else:
        i += 1
print(f"Простые множетели числа: {spisok}")


# 2 вариант
def dividers(a: int, uniq: bool = False) -> list[int]:
    """"Возвращает список простых делителей числа
    uniq = True вернет список уникальных делителей"""
    i = 2
    dividers = []
    while a != 1:
        while a % i == 0:
            dividers.append(i)
            a //= i
        i += 1
    if uniq:
        return list(set(dividers))
    else:
        return dividers


a = int(input("Введите число а: "))
print(f'Список натуральных делителей числа {a}: {dividers(a)}')
print(f"Простые уникальных делителей числа {a}: {dividers(a, True)}")
