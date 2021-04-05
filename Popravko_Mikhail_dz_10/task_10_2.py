"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.

Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
классы для основных классов проекта и проверить работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}, необходимо ткани {self.get_material()}"

    @abstractmethod
    def get_material(self):
        pass

    @property
    def material(self):
        return self.get_material()


class Coat(Clothes):
    def __init__(self, name, size):
        self.size = size
        super().__init__(name)

    def get_material(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        self.height = height
        super().__init__(name)

    def get_material(self):
        return 2 * self.height + 0.3


coat_1 = Coat('coat_1', 65)
coat_2 = Coat('coat_2', 130)

suit_1 = Suit('suit_1', 2)
suit_2 = Suit('suit_2', 3)

print(coat_1)
print(coat_2)
print(suit_1)
print(suit_2)

print("Всего: ", coat_1.material + coat_2.material + suit_1.material + suit_2.material)
