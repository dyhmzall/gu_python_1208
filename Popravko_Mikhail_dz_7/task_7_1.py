"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

import json
import os

CONFIG_FILE = "task_7_1/starter.config.json"
CONFIG_TYPE_FILE = "file"
CONFIG_TYPE_DIR = "dir"
CONFIG_ROOT_DIR = "task_7_1"


def get_starter_config(config_filename):
    """ конфигурация хранится в json-файле, каждый из элементов будет представлять собой объект с параметрами:
    name - название,
    type (file/dir) - тип, файл или директория,
    dirs (только для папок) - вложенные объекты"""
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def create_file(filename):
    if os.path.exists(filename):
        print(f"Файл {filename} уже существует!")
    else:
        with open(filename, "w", encoding="utf-8"):
            print("Создан файл ", filename)


def create_dir(directory_name):
    if os.path.exists(directory_name):
        print(f"Директория {directory_name} уже существует!")
    else:
        os.mkdir(directory_name)
        print("Создана директория ", directory_name)


def starter_initialize(starter_config, root):
    for item in starter_config:
        item_name = item["name"]
        item_type = item["type"]

        if item_type == CONFIG_TYPE_FILE:
            create_file(os.path.join(root, item_name))

        if item_type == CONFIG_TYPE_DIR:
            create_dir(os.path.join(root, item_name))
            inner_items = item["items"]
            # рекурсивный вызов
            starter_initialize(inner_items, os.path.join(root, item_name))


starter_config = get_starter_config(CONFIG_FILE)
starter_initialize(starter_config, CONFIG_ROOT_DIR)
