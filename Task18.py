# Задайте список.
# Напишите программу, которая определит, присутствует ли в заданном списке строк числовое значение.
# ['ssss', 'sngujn556', 56] -> Yes ['56', 'sgnbsb'] -> No

# 1 Вариант
list = ['ssss', 'sngujn556', '?', '1234', '++']
n = 0
for i in list:
    if type(i) == int or type(i) == float:
        n += 1
if n > 0:
    print(f'{list} -> Yes')
else:
    print(f'{list} -> No')

# Вариант 2

mass = ['ssss', 'sngujn556', '44', 258]
types = [str(type(i)) for i in mass]
if "<class 'int'>" in types or "<class 'float'>" in types:
    print(f'{mass} -> Yes')
else:
    print(f'{mass} -> No')
