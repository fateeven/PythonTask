# программа, которая принимает на вход число и проверяет,
# кратно ли оно ((5 и 10) или 15), но не 30. 20 -> Ok 45 -> Ok 150 -> Not Ok

def multiplicity_or():
    s = int(input('Введите число: '))
    if (s % 5 == 0 and s % 10 == 0 or s % 15 == 0) and not s % 30 == 0:
        print('Ок')
    else:
        print('Not Ок')


multiplicity_or()