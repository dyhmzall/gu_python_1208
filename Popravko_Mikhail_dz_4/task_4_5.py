"""
5. *(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
python task_4_5.py USD
75.18, 2020-09-05
"""

import utils
import sys

currency = sys.argv[1]

rate, date = utils.currency_rates(currency)
if rate:
    print(f"Курс валюты '{currency}' составляет {rate} {utils.CURRENCY_RUB} по состоянию на {date}")
else:
    print(f"Курс для валюты '{currency}' не найден")
