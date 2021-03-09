"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
"""

import utils

for currency in [
    utils.CURRENCY_USD,
    utils.CURRENCY_EUR,
    utils.CURRENCY_CNY,
    "usd",
    "non",
]:
    rate, date = utils.currency_rates(currency)
    if rate:
        print(f"Курс валюты '{currency}' составляет {rate} {utils.CURRENCY_RUB} по состоянию на {date}")
    else:
        print(f"Курс для валюты '{currency}' не найден")

