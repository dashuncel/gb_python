'''
3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
'''

num = 0
try:
    num = int(input("Введите число: "))
except ValueError:
    print('Это не число. Выходим.')
    exit(0)

word = ''
digit = num % 10.

if digit in [0, 5, 6, 7, 8, 9]:
    word = 'процентов'
elif digit == 1:
    if num % 100 == 11:
        word = 'процентов'
    else:
        word = 'процент'
elif digit in [2, 3, 4]:
    if num % 100 < 20 and num % 100 > 10:
        word = 'процентов'
    else:
        word = 'процента'

print('{0} {1}'.format(num, word))
