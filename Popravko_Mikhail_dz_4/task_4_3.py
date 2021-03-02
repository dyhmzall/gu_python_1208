"""
3. *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""

from requests import get, utils
import xml.dom.minidom as minidom
import datetime

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

    date_list = doc.getElementsByTagName("ValCurs")[0].getAttribute("Date").split(".")
    date = datetime.date(*map(int, date_list[::-1]))

    for element in doc.getElementsByTagName("Valute"):
        code = element.getElementsByTagName("CharCode")[0].firstChild.nodeValue
        value = element.getElementsByTagName("Value")[0].firstChild.nodeValue

        if code == currency:
            return float(value.replace(",", ".")), date
    else:
        return None, date


for currency in [
    CURRENCY_USD,
    CURRENCY_EUR,
    CURRENCY_CNY,
    "usd",
    "non",
]:
    rate, date = currency_rates(currency)
    if rate:
        print(f"Курс валюты '{currency}' составляет {rate} {CURRENCY_RUB} по состоянию на {date}")
    else:
        print(f"Курс для валюты '{currency}' не найден")
