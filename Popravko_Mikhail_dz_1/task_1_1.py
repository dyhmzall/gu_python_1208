"""
1. Реализовать вывод информации о промежутке времени
в зависимости от его продолжительности duration в секундах:

до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
"""

# в расчетах используются константы
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = SECONDS_IN_MINUTE * 60
SECONDS_IN_DAY = SECONDS_IN_HOUR * 24
SECONDS_IN_MONTH = SECONDS_IN_DAY * 30
SECONDS_IN_YEAR = SECONDS_IN_MONTH * 12

duration = int(input("Введите промежуток времени (в секундах): "))

seconds = duration % SECONDS_IN_MINUTE
minutes = (duration % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
hours = (duration % SECONDS_IN_DAY) // SECONDS_IN_HOUR
days = (duration % SECONDS_IN_MONTH) // SECONDS_IN_DAY
months = (duration % SECONDS_IN_YEAR) // SECONDS_IN_MONTH
years = duration // SECONDS_IN_YEAR

print(f"{duration} секунд это")

text = ""

if years:
    text += f"{years} лет(год/года) "

if months:
    text += f"{months} мес "
elif text:
    text += "0 мес "

if days:
    text += f"{days} дн "
elif text:
    text += "0 дн "

if hours:
    text += f"{hours:02} ч "
elif text:
    text += "0 ч "

if minutes:
    text += f"{minutes:02} мин "
elif text:
    text += "0 мин "

if seconds:
    text += f"{seconds:02} сек "
elif text:
    text += "0 сек "

print(text)
