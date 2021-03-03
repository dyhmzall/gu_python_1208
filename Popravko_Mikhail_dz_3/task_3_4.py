"""
4. *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
в которых фамилия начинается с соответствующей буквы.
Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?
"""


def thesaurus_adv(*args):
    """Возвращает словать из имен и фамилий сотрудников"""

    employee_dict = dict()

    for element in args:

        name, surname = element.split()

        if not employee_dict.get(surname[0]):  # инициализируем элемент словаря по фамилии, если его еще нет
            employee_dict[surname[0]] = dict()

        if not employee_dict[surname[0]].get(name[0]):  # инициализируем элемент словаря по имени, если его еще нет
            employee_dict[surname[0]][name[0]] = list()

        employee_dict[surname[0]][name[0]].append(element)

    return employee_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
