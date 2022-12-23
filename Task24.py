# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fib(n):  # Возвращает член последовательности Фибоначчи
    if n in [1, 2]:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)


def neg_fib(n: int) -> int:  # Возвращает член последовательности Негафибоначчи
    return (-1) ** (n + 1) * fib(n)


def sequence_of_fibs(n: int) -> list[int]:  # генерируем 2 списка и сращиваем их
    list1 = [neg_fib(i) for i in range(n + 1)][::-1]
    list2 = [fib(i) for i in range(1, n + 1)]
    return list1 + list2


n = 8
print(sequence_of_fibs(n))
