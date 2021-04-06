"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц). Результатом
сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и пр.
"""


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = ""
        for i in self.data:
            result += "|"
            for j in i:
                result += "%s" % str(j).center(6)
            result += "|\n"
        return result if result else "[]"

    def __add__(self, other):
        # если матрицы не одинаковые - возвращаем пустую матрицу
        if len(self.data) != len(other.data):
            return Matrix([])

        new_data = list()
        for i, _ in enumerate(self.data):
            if len(self.data[i]) != len(other.data[i]):
                return Matrix([])

            sub_new_data = list()
            for j, _ in enumerate(self.data[i]):
                sub_new_data.append(self.data[i][j] + other.data[i][j])
            new_data.append(sub_new_data)
        return Matrix(new_data)


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[9, 8], [3, 7], [9, 4]])
matrix_3 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])

print("Matrix 1:", matrix_1, sep="\n")
print("Matrix 2:", matrix_2, sep="\n")
print("Matrix 3:", matrix_3, sep="\n")
print("Matrix 1 + Matrix 2:", matrix_1 + matrix_2, sep="\n")
print("Matrix 1 + Matrix 3:", matrix_1 + matrix_3, sep="\n")
