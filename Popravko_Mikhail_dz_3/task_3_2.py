"""
2. *(вместо задачи 1)
Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
"""


def num_translate_adv(number):
    """Переводит числительные от 0 до 10 с английского на русский язык c учетом регистра"""

    # лучше всего хранить переводы в словаре, потому что сложность поиск в соваре O(1)
    numbers = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }

    translate_number = numbers.get(number.lower())  # если элемента нет - возвращает None

    if translate_number is None:
        return translate_number

    return translate_number.capitalize() if number[0].isupper() else translate_number


print("Zero", num_translate_adv("Zero"))
print("one", num_translate_adv("one"))
print("Nine", num_translate_adv("Nine"))
print("eleven", num_translate_adv("eleven"))
