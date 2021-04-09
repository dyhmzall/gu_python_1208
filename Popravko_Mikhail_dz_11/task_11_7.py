"""
7. Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку
методов сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса
(комплексные числа), выполнить сложение и умножение созданных экземпляров.
Проверить корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        return f"{self.real_part} + {self.imaginary_part}j"

    def __add__(self, other):
        self.__check_type(other)
        return ComplexNumber(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)

    def __mul__(self, other):
        self.__check_type(other)
        real_part = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        imaginary_part = self.real_part * other.real_part + self.imaginary_part * other.imaginary_part
        return ComplexNumber(real_part, imaginary_part)

    @staticmethod
    def __check_type(other):
        if not isinstance(other, ComplexNumber):
            raise ValueError("Складывать можно только комплексные числа!")


number_1 = ComplexNumber(10, 20)
number_2 = ComplexNumber(15, 30)
print("number_1 =", number_1)
print("number_2 =", number_2)
print("number_1 + number_2 =", number_1 + number_2)
print("number_1 * number_2 =", number_1 * number_2)
