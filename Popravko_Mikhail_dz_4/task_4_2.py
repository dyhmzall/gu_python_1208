"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...) и возвращающую
курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
"""

from requests import get, utils
import xml.dom.minidom as minidom

CURRENCY_URL = "http://www.cbr.ru/scripts/XML_daily.asp"
CURRENCY_USD = "USD"
CURRENCY_EUR = "EUR"
CURRENCY_CNY = "CNY"
CURRENCY_RUB = "RUB"


def currency_rates(currency=CURRENCY_USD):
    currency = currency.upper()

    response = get(CURRENCY_URL)

    if response.status_code != 200:  # если ответ не 200, значит мы не загрузили текущие курсы валют
        return

    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    doc = minidom.parseString(content)

    for element in doc.getElementsByTagName("Valute"):
        code = element.getElementsByTagName("CharCode")[0].firstChild.nodeValue
        value = element.getElementsByTagName("Value")[0].firstChild.nodeValue

        if code == currency:
            return float(value.replace(",", "."))


for currency in [
    CURRENCY_USD,
    CURRENCY_EUR,
    CURRENCY_CNY,
    "usd",
    "non",
]:
    rate = currency_rates(currency)
    if rate:
        print(f"Курс валюты '{currency}' составляет {rate} {CURRENCY_RUB}")
    else:
        print(f"Курс для валюты '{currency}' не найден")
