"""
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов
по данным файла логов из предыдущего задания.

Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
размер которых превышает объем ОЗУ компьютера.
"""


def get_logs_gen(file):
    """Генератор строк из файла"""
    for line in file:
        data = line.split()
        yield data[0], data[5].strip('"'), data[6]


def get_users(gen):
    """принимает генератор файла и отдает пользователь с количество запросов"""
    data = {}  # используем для хранения кто сколько запросов сделал словарь

    for ip, _, _ in gen:
        if ip in data:
            data[ip] = data[ip] + 1
        else:
            data[ip] = 1

    return data


def get_max_dict(dictionary):
    """возвращает максимальные значения из словаря"""
    """честно украдено с https://ru.stackoverflow.com/questions/759476/найти-максимальное-значение-словаря-python"""
    return {x: y for x, y in filter(lambda x: dictionary[x[0]] == max(dictionary.values()), dictionary.items())}


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    logs_gen = get_logs_gen(f)
    users = get_users(logs_gen)
    print("Всего пользователей: ", len(users))
    spamers = get_max_dict(users)
    print("Спамеры: ", spamers)
