'''
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
'''

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'Скорость машины превышена: {self.speed}')
        else:
            print(f'Текущая скорость: {self.speed}')

class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'Скорость машины превышена: {self.speed}')
        else:
            print(f'Текущая скорость: {self.speed}')

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

town_car = TownCar(100, 'красная', 'Ferrary', True)
police_car = PoliceCar(120, 'синяя', 'lexus', True)
work_car = WorkCar(150, 'зеленая', 'BMW', True)
sport_car = SportCar(90, 'белая', 'Toyota', True)

town_car.show_speed()
police_car.show_speed()
work_car.show_speed()
sport_car.show_speed()






