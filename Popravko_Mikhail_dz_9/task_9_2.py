"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    __weight = 25  # удельный вес 1 кв м
    __thickness = 5  # толщина

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_weight(self):
        return self.__weight * self.__thickness * self._length * self._width


length = 5000  # метров
width = 20  # метров

road = Road(length, width)
print(road.calculate_weight(), 'кг')
