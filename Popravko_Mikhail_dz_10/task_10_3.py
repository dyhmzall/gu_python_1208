"""
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка». В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
(__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и округление до целого числа деления клеток соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
"""


class Cell:
    def __init__(self, name, partition):
        self.name = name
        self.partition = partition

    def __add__(self, other):
        self.check_other(other)
        return Cell("новая клетка", self.partition + other.partition)

    def __str__(self):
        return f"клетка '{self.name}', количество ячеек {self.partition}"

    def __sub__(self, other):
        self.check_other(other)
        partition_sub = self.partition - other.partition
        if partition_sub < 0:
            raise ValueError("Нельзя отнимать от меньшей клетки большую!")
        return Cell("новая клетка", partition_sub)

    def __mul__(self, other):
        self.check_other(other)
        return Cell("новая клетка", self.partition * other.partition)

    def __floordiv__(self, other):
        self.check_other(other)
        return Cell("новая клетка", self.partition // other.partition)

    def check_other(self, other):
        if not isinstance(other, Cell):
            raise ValueError("Операция возможно только с двумя клетками!")

    def make_order(self, count):
        result = []
        for i in range(0, self.partition // count):
            result.append("*" * count)
        if self.partition % count:
            result.append("*" * (self.partition % count))
        return "\n".join(result)


cell_1 = Cell("клетка 1", 30)
cell_2 = Cell("клетка 2", 15)

print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
# print(cell_2 - cell_1) # тут будет ошибка
# print(cell_1 + 1) # тут будет ошибка
print(cell_1 * cell_2)
print(cell_1 // cell_2)

print("cell_1.make_order(3)", cell_1.make_order(3), sep="\n")
print("cell_1.make_order(4)", cell_1.make_order(4), sep="\n")
print("cell_1.make_order(7)", cell_1.make_order(7), sep="\n")
