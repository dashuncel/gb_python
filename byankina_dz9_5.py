'''
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Ручка {self.title} рисует синим')

class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш {self.title} рисует серым')

class Handle(Stationery):
    def draw(self):
        print(f'Маркер {self.title} рисует любым цветом')

my_pen = Pen('ErichCrauser')
my_pencil = Pencil('Map')
my_handle = Handle('Bruno Visconti')

my_pen.draw()
my_pencil.draw()
my_handle.draw()