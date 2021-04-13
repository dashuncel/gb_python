'''
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
 num_translate("one")
"один"
num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.

* Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"

'''

def num_translate_adv(num):
    if type(num) != str:
        return 'Error'

    vocabulary = {
        'one': 'один',
        'two':  'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    return vocabulary.get(str(num).lower(), num)


print(num_translate_adv(10))
print(num_translate_adv('One'))
print(num_translate_adv('Ten'))

