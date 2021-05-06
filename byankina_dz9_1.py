'''
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
from time import sleep

class TrafficLights():
    __color_list = ['красный', 'желтый', 'зеленый']
    __color_delay = [7, 3, 2]

    def __init__(self, color):
        self.__color = color
        self.timer = self.__color_list.index(self.__color)

    def running(self):
        idx = self.__color_list.index(self.__color) + 1
        if idx > len(self.__color_list) - 1:
            idx = 0

        self.__color = self.__color_list[idx]
        print(f'Горит {self.__color} на {self.__color_delay[idx]} сек.')
        sleep(self.__color_delay[idx])


my_traffic = TrafficLights('красный')
i = 0
while True:
    if i > 9:
        break
    my_traffic.running()
    i += 1



