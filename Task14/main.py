# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Enter a number above 1 for check: '))
pow_of_2 = 2
if n >= pow_of_2:
    i = 1
    print(f'Powers of 2 that not above {n}:')
    while pow_of_2 <= n:
        print(f'2^{i} = {pow_of_2}')
        pow_of_2 = pow_of_2 * 2
        i += 1
    print('Thanks for using products of Tardy Inc.')
else:
    print(f'{n} is less than 2, sorry. ')
