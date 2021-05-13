'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
 одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Wear(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass


class Coat(Wear):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def __str__(self):
        return f'{self.name}, расход {self.consumption} метров ткани на размер {self.size}'

    @property
    def consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Wear):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def consumption(self):
        return round(2 * self.height + 0.3, 2)

    def __str__(self):
        return f'{self.name}, расход {self.consumption} метров ткани на рост {self.height}'


myCoat = Coat('Мое пальто', 48)
print(myCoat.consumption)
print(myCoat)

mySuit = Suit('Мое пальто', 48)
print(mySuit.consumption)
print(mySuit)


