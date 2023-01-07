# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# Первое решение
N = int(input('Введите число: '))
s = 1
while s < N+1:
    print(f'{s}: {s * 3 + 1} ', end=', ')
    s += 1

print()  # /------

# Второе решение
n = int(input('Введите число: '))
for i in range(1, n + 1):
    print(f'{i}: {i * 3 + 1} ', end=', ')

print()  # /------

# Третье решение
def dictionary_with_multiple():
    n = int(input('Введите число: '))
    dict = {}
    for i in range(1, n+1):
        res = i * 3 + 1
        dict[i] = res
    print(f'Для n = {n}: {dict}')


dictionary_with_multiple()

# Четвертое решение
def dictionary_with_multiple2():
    n = int(input('Введите число: '))
    print({n: 3*n+1 for n in range(n)})


dictionary_with_multiple2()