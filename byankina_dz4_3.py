'''
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
str, решить поставленную задачу? Функция должна возвращать результат числового типа,
например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
выведите курсы доллара и евро.
3. *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
'''

import requests
import xml.etree.cElementTree as ET
import datetime

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

def request_rates():
    data = ''
    cur_dict = dict()

    request = requests.get(URL)
    if request.status_code != 200:
        return 'Error' + request.status_code

    xmldoc = ET.fromstring(request.text)
    day, month, year = map(int, xmldoc.get('Date').split('.'))
    data = datetime.datetime(year, month, day)
    cur_dict['data'] = data
    for child in xmldoc.findall('Valute'):
        cur_dict[child.find('CharCode').text]  = float(child.find('Value').text.replace(',','.'))
    return cur_dict


def currency_rates(code_curr):
    code_curr = code_curr.upper()
    currencies = request_rates()
    return f'Курс {code_curr} на {currencies.get("data")} = {currencies.get(code_curr)}'

print(currency_rates("USD"))
print(currency_rates("eur"))


