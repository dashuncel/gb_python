'''
5. Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]
A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде
<r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки,
как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп
или 00 коп).
B. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что
объект списка после сортировки остался тот же).
C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по
возрастанию, написав минимум кода?
'''
import random

#генерация
i = 0
price_list = []
while i < 25:
    i += 1
    price_list.append((random.random() * 100).__round__(2))

print('Сгенерирован список: {}'.format(price_list))

#A.
print(' ,'.join(map(lambda x: str('{} руб {} коп.'.format(str(x).split('.'))), price_list)))

#B.
print('Отсортированный список: {}'.format(sorted(price_list)))
print('Исходный список: {}'.format(price_list))

#C.
#new_price = price_list.sort(reverse=True)
#print('Новый отсортированный по убыванию список: {}'.format(new_price))

#D.


