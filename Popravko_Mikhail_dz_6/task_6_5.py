"""
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь
к обоим исходным файлам и путь к выходному файлу со словарём.
Проверить работу скрипта для случая, когда все файлы находятся в разных папках.

Использованы значения для путей
Введите относительный путь до файла с пользователями: users/users.csv
Введите относительный путь до файла с хобби: hobbies/hobby.csv
Введите относительный путь до файла с данными пользователей: info/info.no_json
"""
import json


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


users_filename = 'task_5/' + input("Введите относительный путь до файла с пользователями: ")
hobbies_filename = 'task_5/' + input("Введите относительный путь до файла с хобби: ")
info_filename = 'task_5/' + input("Введите относительный путь до файла с данными пользователей: ")

users_gen = get_generator_from_file(users_filename)
hobbies_gen = get_generator_from_file(hobbies_filename)

info_gen = get_info_generator(users_gen, hobbies_gen)

save_info(info_filename, info_gen)

new_info_gen = get_info_generator_from_file(info_filename)

for item in new_info_gen:
    print(item, type(item), item["name"], item["surname"], item["middle_name"], item["hobbies"])
