'''
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
'''
'''
RE_NAME1 = re.compile(r'^[А-ЯЁ][а-яё]+$')
RE_NAME2 = re.compile(r'^[А-ЯЁ][а-яё]{2,}$')
REG_DATA = re.compile(r'^(?:\d{2}\.){2}\d{4}$')
print(RE_NAME1.match(name))
декторатор
def p_wrapper(func):
    def tag_wrapper(*args, **kwargs):
        markup = func(*args, **kwargs)
        return f'<p>{markup}</p>'
    return tag_wrapper
'''

import re
def email_parse(email):
    RE_EMAIL = re.compile(r'^[a-z\d]+\@(\w+\.)+\w+', re.IGNORECASE)
    tested = RE_EMAIL.match(email)
    if tested:
        my_dict = dict(zip(['username', 'domain'], tested.group(0).split('@')))
    else:
        raise ValueError(0)
    return my_dict

print(email_parse('someone@geekbrains.ru'))
print(email_parse('aaaa121'))



