"""
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида:
'Привет, Игорь!'
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
Можно ли при этом не создавать новый список?
"""

employees = [
    'инженер-конструктор Игорь',
    'главный бухгалтер МАРИНА',
    'токарь высшего разряда нИКОЛАй',
    'директор аэлита'
]

for element in employees:
    *_, employee = element.split()  # в методичке указано, что для мусора можно использовать имя переменной "_"
    print(f"Привет, {employee.capitalize()}!")