'''
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
'''

import re

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
idx = 0

while True:
    elem = my_list[idx]
    try:
        num = int(elem)
        if elem.startswith('+') or elem.startswith('-'):
           my_list[idx] = elem[0] + '{0:02}'.format(num)
        else:
           my_list[idx] = '{0:02}'.format(num)
        my_list.insert(idx, '"')
        my_list.insert(idx + 2, '"')
        idx += 3
    except ValueError:
        idx += 1
    if idx >= len(my_list):
        break

my_str = ' '.join(my_list)
print(my_str)

for sym in enumerate(range(len(my_str))):
    print(sym)

#my_str = re.sub('"\s\d+', r'\1', my_str)
#my_str = re.sub('\d\s+"', r'', my_str)
#print(my_str)