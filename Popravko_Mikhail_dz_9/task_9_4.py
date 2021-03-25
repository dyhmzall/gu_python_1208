"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Скорость машины {self.name} {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Машина {self.name} превышает допустимую скорость")
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Машина {self.name} превышает допустимую скорость")
        else:
            super().show_speed()


class PoliceCar(Car):
    pass


town_car = TownCar(70, "черная", "Ford", False)
sport_car = SportCar(180, "красная", "F1", False)
work_car = WorkCar(30, "белая", "Audi", False)
police_car = PoliceCar(90, "синяя", "VAZ", True)

town_car.go()
town_car.show_speed()
town_car.stop()

sport_car.go()
sport_car.show_speed()
sport_car.turn("направо")
sport_car.stop()
