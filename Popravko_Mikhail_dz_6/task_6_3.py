"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл. Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше записей,
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""
import json

USERS_FILENAME = "task_3/users.csv"
HOBBIES_FILENAME = "task_3/hobby.csv"
INFO_FILENAME = "task_3/info.json"


def get_lines_from_file(filename):
    """Прочитать файл и вернуть массив строк"""
    with open(filename, "r", encoding="utf-8") as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def make_info(users, hobbies):
    """Составить словарь с данными из списков пользователей и хобби"""
    return {users[i]: hobbies[i] if i < len(hobbies) else None for i in range(len(users))}


def save_info(filename, info):
    """Сохранить словать с данными пользователя в файл"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(info, f)


def get_info(filename):
    """Получить словать с данными пользователя из файла"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


users = get_lines_from_file(USERS_FILENAME)
hobbies = get_lines_from_file(HOBBIES_FILENAME)

print("Пользователи: ", users)
print("Хобби: ", hobbies)

if len(users) < len(hobbies):
    exit(1)

info = make_info(users, hobbies)

print("Информация: ", info)

save_info(INFO_FILENAME, info)

new_info = get_info(INFO_FILENAME)
print("Информация из файла JSON: ", new_info)

print("Проверка, что данные - это словарь:")
for key, value in new_info.items():
    print(key, value, sep=" - ")
