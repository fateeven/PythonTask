# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
from sympy import simplify

from polinom_functions_for_task32_and_task33 import create_pol_file
from polinom_functions_for_task32_and_task33 import create_polinom
import sympy

k = int(input('Задайте степень: '))

pol1 = create_polinom(k)  # генерируем полиномы
pol2 = create_polinom(k)

filename1 = 'Task33_first'  # имена создоваемых текстовых файлов
filename2 = 'Task33_second'
sum_filename = 'Task33_sum_polinoms'

create_pol_file(pol1, filename1)  # создаем файлы с полиномами
create_pol_file(pol2, filename2)

with open(f'{filename1}.txt', 'r') as f1:  # считываем данные из файла Task33_first
    f_pol = f1.read()
    print(f'Первый полином: {f_pol}')

with open(f'{filename2}.txt', 'r') as f2:  # считываем данные из файла Task33_second
    s_pol = f2.read()
    print(f'Первый полином: {s_pol}')

sum_of_polinoms = simplify(f_pol + '+' + s_pol)  # складываем полниномы
sum_of_polinoms = str(sum_of_polinoms)
print(f'Сумма полиномов: {sum_of_polinoms}')

with open(f'{sum_filename}.txt', 'w') as s:  # записываем сумму полиномов в файл Task33_sum_polinoms
    s.write(sum_of_polinoms)
