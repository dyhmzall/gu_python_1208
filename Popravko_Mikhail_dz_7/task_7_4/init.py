"""
скрипт для создания рандомных файлов для задачи 4
"""

import random
import os
import shutil

FILE_COUNT = 16
FILE_NAME_LETTER_COUNT = 8
FILE_CONTENT_MIN_COUNT = 0
FILE_CONTENT_MAX_COUNT = 100000
FILE_DIR = "data"

# удаляем старые файлы
shutil.rmtree(FILE_DIR)
os.mkdir(FILE_DIR)

random_sample_list = [chr(symbol) for symbol in range(ord('a'), ord('z'))]

for _ in range(FILE_COUNT):
    filename = os.path.join(FILE_DIR, ''.join(random.sample(random_sample_list, FILE_NAME_LETTER_COUNT)) + '.bin')
    with open(filename, "w", encoding="utf-8") as f:
        f.write('d' * random.randint(FILE_CONTENT_MIN_COUNT, FILE_CONTENT_MAX_COUNT))
