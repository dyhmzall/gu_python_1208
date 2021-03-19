"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django.
"""

import os
import shutil

ROOT_DIR = r"task_7_3\my_project"
TEMPLATE_DIR = r"task_7_3\my_project\template"


def move_template(filename):
    rel_filename = os.path.relpath(filename, os.path.dirname(os.path.dirname(filename)))
    rel_dirname = os.path.join(TEMPLATE_DIR, os.path.dirname(rel_filename))
    os.makedirs(rel_dirname, exist_ok=True)
    shutil.copy2(filename, os.path.join(rel_dirname, os.path.basename(filename)))


for root, dirs, files in os.walk(ROOT_DIR):
    # исключим из обхода саму директорию template
    if os.path.relpath(root, ROOT_DIR).startswith(r"template"):
        continue

    for file in files:
        if file.lower().endswith('.html'):
            move_template(os.path.join(root, file))
