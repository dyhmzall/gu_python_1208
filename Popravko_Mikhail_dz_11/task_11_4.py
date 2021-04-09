"""
Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведённых типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
"""


class Depot:
    def __init__(self, name, country, city, address):
        self.name = name
        self.country = country
        self.city = city
        self.address = address


class OfficeEquipment:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        print_array = list()
        for key, value in self.__dict__.items():
            print_array.append(f"{key}={value}")
        return ", ".join(print_array)


class Printer(OfficeEquipment):
    def __init__(self, name, size, color_type, speed):
        super().__init__(name, size)
        self.color_type = color_type
        self.speed = speed


class Scanner(OfficeEquipment):
    def __init__(self, name, size, quantity):
        super().__init__(name, size)
        self.quantity = quantity


class Xerox(OfficeEquipment):
    def __init__(self, name, size, color_type, speed, quantity):
        super().__init__(name, size)
        self.color_type = color_type
        self.speed = speed
        self.quantity = quantity


hp_1 = Printer('hp_1', '100x200', 'black', '60')
print(hp_1)
