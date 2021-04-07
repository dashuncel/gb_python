'''
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
'''

time_stamp = ''

def get_year(digit):
    #на вход даем количество дней
    return [digit // 365, digit % 365]

def get_minutes(digit):
    # на вход даем количество секунд
    return [digit // 60, digit % 60]

def get_days(digit):
    # на вход даем количество часов
    return [digit // 24, digit % 24]

def get_hours(digit):
    # на вход даем количество минут
    return [digit // 60, digit % 60]

while True:
    time_stamp = input("Введите время в секундах: ")
    if time_stamp.isdigit():
        time_stamp = int(time_stamp)
        break

minutes = get_minutes(time_stamp)
hours = get_hours(minutes[0])
days = get_days(hours[0])
years = get_days(days[0])

print('В {0} секундах {1} years, {2} days, {3} hours, {4} min, {5} sec'.format(time_stamp, years[0], years[1], days[1], hours[1], minutes[1]))

