"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
import time
import datetime


class Date:
    date = ""
    days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    def __init__(self, date):
        Date.date = date

    @classmethod
    def get_timestamp(cls):
        return time.mktime(datetime.datetime.strptime(cls.date, "%d-%m-%Y").timetuple())

    @staticmethod
    def validate():
        date_obj = datetime.datetime.strptime(Date.date, "%d-%m-%Y")

        # считаем корректным год от 1 до 9999
        if 1 <= date_obj.year >= 9999:
            return False

        # считаем корректным месяц от 1 до 12
        if 1 <= date_obj.month >= 12:
            return False

        # учтем, что в высокостном году есть 29 февраля
        if date_obj.year % 4:
            Date.days[2] = 29
        else:
            Date.days[2] = 28

        # проверяем день - от 1 до максимального количества в зависимости от месяца
        if 1 <= date_obj.day >= Date.days[date_obj.month]:
            return False

        return True


date_1 = Date("07-04-2021")
print("Корректная дата: ", date_1.validate())
print("Timestamp: ", date_1.get_timestamp())

date_2 = Date("28-02-2021")
print("Корректная дата: ", date_2.validate())
print("Timestamp: ", date_2.get_timestamp())
