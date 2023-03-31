"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите
минимальное количество монет, которые нужно перевернуть
"""

N = int(input('Enter a number of coins:'))
obv = 0
for i in range (0, N):
    side = int(input('Enter 1 for obverse of coin and 0 for back side:'))
    if side==1:
        obv += 1
print('Minimal flips for getting the same sides:')
print(obv if N/2>obv else N-obv)