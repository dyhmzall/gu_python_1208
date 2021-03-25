"""
4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
Также реализовать парсинг данных из файлов - получить отдельно фамилию, имя и отчество для пользователей
и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
В словаре должны храниться данные, полученные в результате парсинга.
"""
import json

USERS_FILENAME = "task_4/users.csv"
HOBBIES_FILENAME = "task_4/hobby.csv"
INFO_FILENAME = "task_4/info.not_json"  # в каждой строке этого файла будет валидный JSON, но целиком это не JSON


def get_generator_from_file(filename):
    """получить генератор строк из файла"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def get_info_generator(users_generator, hobbies_generator):
    """получить генератор информации о пользователях"""

    for fio in users_generator:
        surname, name, middle_name = fio.split(",")

        try:
            hobby = next(hobbies_generator).split(",")
        except StopIteration:
            hobby = None

        yield {
            "name": name,
            "surname": surname,
            "middle_name": middle_name,
            "hobbies": hobby
        }

    # обработка ситуации, когда файл с хобби имеет больше данных, чем файл с юзерами
    try:
        next(hobbies_generator)
        exit(1)  # если в генератор хобби что-то есть, значит имеем ошибку
    except StopIteration:
        pass  # ничего не делаем


def save_info(filename, info):
    """Сохранить данные пользователей в файл, info - генератор"""
    with open(filename, "w", encoding="utf-8") as f:
        for data in info:
            f.writelines(json.dumps(data) + "\n")


def get_info_generator_from_file(filename):
    """получить генератор информации о пользователях из файла"""
    with open(filename, "r", encoding="utf-8") as f:
        for data in f:
            yield json.loads(data.strip())


users_gen = get_generator_from_file(USERS_FILENAME)
hobbies_gen = get_generator_from_file(HOBBIES_FILENAME)

info_gen = get_info_generator(users_gen, hobbies_gen)

save_info(INFO_FILENAME, info_gen)

new_info_gen = get_info_generator_from_file(INFO_FILENAME)

for item in new_info_gen:
    print(item, type(item), item["name"], item["surname"], item["middle_name"], item["hobbies"])
