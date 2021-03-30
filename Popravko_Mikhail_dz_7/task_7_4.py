"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os
import collections


def get_file_stat(dir):
    stat = collections.defaultdict(int)
    for root, _, files in os.walk(dir):
        for file in files:
            limit = get_limit_size(os.path.join(root, file))
            stat[limit] += 1
    return stat


def get_limit_size(file):
    """получить границу размера файла"""
    size = os.stat(file).st_size
    test_size = 10
    while True:
        if size < test_size:
            return test_size
        test_size *= 10


dir_for_stat = r"task_7_4\data"
for item_key, item_value in get_file_stat(dir_for_stat).items():
    print(item_key, item_value)
