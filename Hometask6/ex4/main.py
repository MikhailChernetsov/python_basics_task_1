'''
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

'''


class Car:
    max_speed = 100
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'Go-go, {self.color} {self.name} with speed {self.speed}')
        if self.is_police:
            print('Viu - viu - viu!')

    def stop(self):
        print(f'Stop, {self.color} {self.name}')

    def turn(self, direction):
        print(f'{self.color} {self.name} turn {direction}')

    def show_speed(self):
        print(f'Speed of car {self.color} {self.name} is {self.speed}')
        if self.speed > self.max_speed:
            if self.is_police:
                print("Sorry, but I'm official!")
            else:
                print('Your speed is too big! ВАМ ШТРАФ!!!')
        else:
            print("It's ok!")


class TownCar(Car):
    max_speed = 60

    def show_speed(self):
        print(f'Speed of car {self.color} {self.name} is {self.speed}')
        if self.speed > self.max_speed:
            print('Your speed is too big! ВАМ ШТРАФ!!!')
        else:
            print("It's ok!")


class SportCar(Car):
    max_speed = 200


class WorkCar(Car):
    max_speed = 40

    def show_speed(self):
        print(f'Speed of car {self.color} {self.name} is {self.speed}')
        if self.speed > self.max_speed:
            print('Your speed is too big! ВАМ ШТРАФ!!!')
        else:
            print("It's ok!")


class PoliceCar(Car):
    is_police = True


car_1 = WorkCar(100, 'red', 'lada')
car_1.go()
car_1.show_speed()
car_1.turn('left')
car_1.stop()

print()

police_car = PoliceCar(120, 'white-blue', 'kia')
police_car.go()
police_car.turn('right')
police_car.show_speed()

print()

sport_car = SportCar(180, 'red', 'Aston Martin')
sport_car.go()
sport_car.turn('right')
sport_car.show_speed()
sport_car.stop()

print()

car_2 = TownCar(50, 'green', 'opel')
car_2.go()
car_2.turn('right')
car_2.show_speed()
car_2.stop()
