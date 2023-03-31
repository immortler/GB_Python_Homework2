"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""

prod = int(input('Enter product of numbers (P): '))
sum = int(input('Enter sum of numbers (S): '))
first_number = 0
second_number = 0
while first_number * second_number != prod or first_number + second_number != sum:
    first_number += 1
    second_number = prod / first_number
    if first_number == prod and first_number > 1:
        print('Wrong product/sum pair.')
        break
    elif first_number * second_number == prod and first_number + second_number == sum:
        print(f'X = {first_number}, Y = {int(second_number)} ')
