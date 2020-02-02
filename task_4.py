import random


class Car:
    def __init__(self, speed, color, name, is_police=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина едет прямо')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        key = random.randint(0, 2)
        dict = {0: ' поехала обратно', 1: 'поехала направо', 2: 'поехала налево'}
        print(f'Машина {dict[key]}')

    def show_speed(self):
        print(f'Машина едет со сокростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Внимание! Машина едет с превышенной скоростью!')


class SportCar(Car):
    def stop(self):
        print('Спортивная машина остановилась')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Внимание! Машина едет с превышенной скоростью!')


class PoliceCar(Car):
    def go(self):
        print('Полицейская машина едет прямо')

    def turn(self):
        key = random.randint(0, 2)
        dict = {0: ' поехала обратно', 1: 'поехала направо', 2: 'поехала налево'}
        print(f'Полицейская машина {dict[key]}')


car_base = Car(220, 'Черная', 'Жигули')
print(f'Скорость машины: {car_base.speed}')
print(f'Цвет машины: {car_base.color}')
print(f'Марка машины: {car_base.name}')
car_base.go()
car_base.stop()
car_base.turn()
car_base.show_speed()
print()

car_1 = TownCar(150, 'Белая', 'Шкода')
print(f'Скорость машины: {car_1.speed}')
print(f'Цвет машины: {car_1.color}')
print(f'Марка машины: {car_1.name}')
car_1.go()
car_1.stop()
car_1.turn()
car_1.show_speed()
print()

car_2 = SportCar(320, 'Красная', 'Феррари')
print(f'Скорость машины: {car_2.speed}')
print(f'Цвет машины: {car_2.color}')
print(f'Марка машины: {car_2.name}')
car_2.go()
car_2.stop()
car_2.turn()
car_2.show_speed()
print()

car_3 = WorkCar(65, 'Серая', 'Газель')
print(f'Скорость машины: {car_3.speed}')
print(f'Цвет машины: {car_3.color}')
print(f'Марка машины: {car_3.name}')
car_3.go()
car_3.stop()
car_3.turn()
car_3.show_speed()
print()

car_4 = PoliceCar(110, '-', 'Форд', 'да')
print(f'Скорость машины: {car_4.speed}')
print(f'Цвет машины: {car_4.color}')
print(f'Марка машины: {car_4.name}')
car_4.go()
car_4.stop()
car_4.turn()
car_4.show_speed()
print()
