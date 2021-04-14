import requests
import xml.etree.cElementTree as ET
import datetime

def request_rates():

    data = ''
    cur_dict = dict()
    URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

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

